# coding=utf-8
import pandas as pd
import os


from datapipeline.utils.io  import (load_data, write_preprocessed_data, 
									create_file_object, file_object)

raw_repo = 'data/raw/'
preprocess_repo = 'data/preprocess/'
process_repo = 'data/process/'

list_of_files = os.listdir(preprocess_repo)


def find_word_in_text(string, list_of_drug):
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
    	.apply(lambda string : find_word_in_text(string,list_of_drug))
    c_trials = c_trials.apply(lambda x: x.astype(str).str.upper())
    c_trials = c_trials.rename(columns = {"date":"date_mention"})

    return c_trials

def prepare_pubmed (pubmed,list_of_drug):
    pubmed['atccode'] = pubmed['title'].str.upper()\
    	.apply(lambda string : find_word_in_text(string,list_of_drug))
    pubmed = pubmed.apply(lambda x: x.astype(str).str.upper())
    pubmed = pubmed.rename(columns = {"date":"date_mention"})

    return pubmed

def create_journal_ds(c_trials,pubmed):
    journal = pd.concat([pubmed[['journal','date_mention','atccode']],
    	c_trials[['journal','date_mention','atccode']]])
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

	try:

		write_preprocessed_data(processed_journal,"journal",process_repo,"json")
		write_preprocessed_data(drug,"drug",process_repo,"json")
		write_preprocessed_data(prepared_c_trials,"clinical_trials",process_repo,"json")
		write_preprocessed_data(preprared_pubmed,"pubmed",process_repo,"json")

	except:
		print("An error was raised while writting the processed data")

