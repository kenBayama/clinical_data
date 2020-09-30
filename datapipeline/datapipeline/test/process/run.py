# coding=utf-8
import pandas as pd
import os


from datapipeline.utils.io  import (load_data, write_preprocessed_data, 
									create_file_object, file_object)

raw_repo = 'data/test/raw/'
preprocess_repo = 'data/test/preprocess/'
process_repo = 'data/test/process/'

list_of_files = os.listdir(preprocess_repo)


def who_is_there(string, list_of_drug):
    drug_present = []
    for word in list_of_drug:
        if word.upper() in string.upper():
            drug_present.append(list_of_drug[word].strip())
    return  ','.join(map(str, drug_present))

def clean_column(string):
    str2 = list(set(string.split(",")))
    return list(filter(None,str2))

def prepare_c_trials (c_trials,list_of_drug):
    c_trials['atccode'] = c_trials['scientific_title'].str.upper()\
    	.apply(lambda string : who_is_there(string,list_of_drug))
    c_trials = c_trials.apply(lambda x: x.astype(str).str.upper())
    return c_trials

def prepare_pubmed (pubmed,list_of_drug):
    pubmed['atccode'] = pubmed['title'].str.upper()\
    	.apply(lambda string : who_is_there(string,list_of_drug))
    pubmed = pubmed.apply(lambda x: x.astype(str).str.upper())
    return pubmed

def create_journal_ds(c_trials,pubmed):
    journal = pd.concat([pubmed[['journal','date','atccode']],
    	c_trials[['journal','date','atccode']]])
    journal = journal.apply(lambda x: x.astype(str).str.upper())
    journal = journal.groupby('journal')\
    	.agg(lambda column: ",".join(column)).reset_index('journal')
    journal = journal.applymap(clean_column)
    journal ['id']= journal.reset_index().index.astype(str)

    return journal

def prepare_for_drug(dataset,name):
    dataset['atccode'] = dataset['atccode']\
    	.apply(lambda s: s.split(",")).to_frame()

    dataset = dataset.explode('atccode')
    dataset = dataset.groupby('atccode')\
    	.agg(lambda x : ",".join(x)).reset_index('atccode')

    dataset = dataset.rename(columns = {"id":name +"_id"})
    return dataset

def create_dict_of_drug(drug):
	list_of_drug = (drug['drug'] + "," + drug['atccode']).tolist()
	lst = [s.split(",") for s in list_of_drug]
	lst = [{s[0]: s[1]} for s in lst]
	list_of_drug = dict((key,d[key]) for d in lst for key in d)
	return list_of_drug

    

def main():

	list_of_file_object = list(create_file_object(list_of_files,preprocess_repo))
	dict_ds = load_data (list_of_file_object)

	drug = dict_ds["drugs"].dataset
	list_of_drug = create_dict_of_drug(drug)

	"""
	prepare the clinical_trials and pubmed data to create the foreign keys 
	to drugs and for the implementation of the journal table data 

	"""
	try:
		prepared_c_trials = prepare_c_trials(dict_ds['clinicaltrials']\
			.dataset,list_of_drug)

		preprared_pubmed = prepare_pubmed(dict_ds['pubmed'].dataset,list_of_drug)
		
		processed_journal = create_journal_ds(prepared_c_trials,preprared_pubmed)
	except:
		print("An error was raised while preparing the journal data")

	"""
	prepare the journal, clinical ans pubmed data
	 to create the drugs table data with all the right foreign keys
	
	"""
	try:

		pubmed_f_drugs = prepare_for_drug(preprared_pubmed,"pubmed")
		c_trials_f_drugs = prepare_for_drug(prepared_c_trials,"clinical_trials")


		journal_f_drugs = processed_journal.explode('atccode')
		journal_f_drugs = journal_f_drugs.groupby('atccode')\
			.agg(lambda x: ",".join(x)).reset_index('atccode')

		journal_f_drugs = journal_f_drugs.rename(columns= {"id":"journal_id"})
	except:
		print("An error was raised while preparing the journal data")

	try:
		drugs = drug\
			.merge(c_trials_f_drugs[['atccode','clinical_trials_id']],
				on='atccode', how='left')\
			.merge(pubmed_f_drugs[['atccode','pubmed_id']], on= 'atccode', how='left')\
			.merge(journal_f_drugs[['atccode','journal_id']], on= 'atccode', how='left')\
			.fillna("")
	except: 
		print(" An error was raised while preparing the drugs table")

	

	write_preprocessed_data(processed_journal,"journal",process_repo,"json")
	write_preprocessed_data(drugs,"drug",process_repo,"json")
	write_preprocessed_data(prepared_c_trials,"clinical_trials",process_repo,"json")
	write_preprocessed_data(preprared_pubmed,"pubmed",process_repo,"json")


