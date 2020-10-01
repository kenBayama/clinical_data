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
    """
    Description :
        This function allow you to find if a list of word is in a string :
             Turning all letter to uppercase
             Checking the presence of a word in a string
             Removing space
             Appending the new element in a list 
             Transforming a list of string to a string with comma for separation
    Args:
        string: string 
        list_of_drug : dict, key : name of the drug
                             value :  atccode of the drug
    
    Returns:
        output: string
    """
    drug_present = []
    for word in list_of_drug:
        if word.upper() in string.upper():
            drug_present.append(list_of_drug[word].strip())

    return  ','.join(map(str, drug_present))

def clean_column(string):
    """
    Description :
        This function allow you to transform a string separated by comas in a list of string :

            Transforming the string in a list
            Removing the duplicated 
            Removing empty space
    Args:
        string: string 

    Returns:
        output: list of string
    """
    list_of_strng = list(set(string.split(",")))
    list_of_strng = list(filter(None,list_of_strng))

    return list_of_strng


def process_data (dataset,list_of_drug,column_name):
    """
    Description :
        This function allow you to transform the clinicals_trials or pubmed data 
        in order to make the foreign keys to the drug data:

            Finding the drugs name in each scientic title or title column
            Turning every letter in uppercase for later use
            Renaming the date column
    Args:
        c_trials: pandas.dataframe 
        list_of_drug : dict, key : name of the drug
                             value :  atccode of the drug
        column_name : string
    
    Returns:
        output: pandas.dataframe
    """
    dataset['atccode'] = dataset[column_name].str.upper()\
        .apply(lambda string : find_word_in_text(string,list_of_drug))
    dataset = dataset.apply(lambda x: x.astype(str).str.upper())
    dataset = dataset.rename(columns = {"date":"date_mention"})

    return dataset

def create_journal_ds(c_trials,pubmed):
    """
    Description :
        This function allow you to create the journal dataset from the clinicals trials data 
        and the pubmed data :

            keeping only the journal, date_mention and atccode column
            Joining the two dataframe.
            Turning every letter to uppercase
            Grouping by the column journal
            Aggregating by concatenation of string 
            Cleaning by using the clean_column function
            Creating an Index

    Args:
        c_trials: pandas.dataframe 
        pubmed : pandas.dataframe 
    
    Returns:
        output: pandas.dataframe
    """
    journal = pd.concat([pubmed[['journal','date_mention','atccode']],
    	c_trials[['journal','date_mention','atccode']]])
    journal = journal.apply(lambda x: x.astype(str).str.upper())
    journal = journal.groupby('journal')\
    	.agg(lambda column: ",".join(column)).reset_index('journal')
    journal = journal.applymap(clean_column)
    journal ['id']= journal.reset_index().index.astype(str)

    return journal


def create_dict_of_drug(drug):
    """
    Description :
        This function allow you to create a dictionnary linking the name of a drug
        and its atccode: 

            Creating a list of string from concatenation of two columns drug and atccode
            Transforming the list of string in list of list of string
            Converting that list of list in a list of dict
            Converting the list of dict in a dict

    Args:
        drug: pandas.dataframe 
    
    Returns:
        output: dict 
    """
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

	
	#prepare the clinical_trials and pubmed data to create the foreign keys 
	#to drugs and for the implementation of the journal table data 

	

	try:
		prepared_c_trials = process_data(dict_ds['clinicaltrials']\
			.dataset,list_of_drug,"scientific_title")

		preprared_pubmed = process_data(dict_ds['pubmed'].dataset,list_of_drug,
            "title")
		
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

