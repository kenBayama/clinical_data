# coding=utf-8
import pandas as pd
import os
import re


from datapipeline.utils.loggers import Preprocessing_logger
from datapipeline.utils.io  import (load_data, write_preprocessed_data, 
									create_file_object, file_object)
from datapipeline.utils.copy  import copy_csv


def preprocess_c_trials (clinicalT):
    """
    Description :
        This function allow you to clean the raw data from clinical trials source*
        by : 
            Removing the space in the beguinning and the end of the scientific_title column
            Dropping the row with NaN data in it
            Converting the date column into a panda datetime column
            Formatting the datetime column to have the same format for each column
            Cleaning the journal column to remove hexadecimal characters
            Cleaning the  journal column to remove hexadecimal characters

        
    Args:
        pubmed: panda dataframe object
    
    Returns:
        output: panda.dataframe
    """

    clinicalT = clinicalT[clinicalT['scientific_title'].str.strip().map(len)>1].dropna()
    clinicalT_date = pd.to_datetime(clinicalT['date'])
    clinicalT['date'] =  clinicalT_date.dt.strftime('%d/%m/%Y')
    clinicalT['journal'] = clinicalT['journal'].str.replace(r'(\\.*$)','') 
    clinicalT['scientific_title'] = clinicalT['scientific_title'].str.replace(r'(\\.*$)','') 
    return clinicalT

def preprocess_pubmed(pubmed):
    """
    Description :
        This function allow you to clean the raw data from pubmed source by :
            Removing the wrong id and setting a proper one
            Formatting the datetime column to have the same format for each column
            Cleaning the title column by removing unnecessary double quote chracter
        
    Args:
        pubmed: panda dataframe object
    
    Returns:
        output: panda.dataframe

    """
    pubmed = pubmed.drop('id',1)
    pubmed ['id'] = pubmed.reset_index().index
    pubmed['date'] = pd.to_datetime(pubmed['date']).dt.strftime('%d/%m/%Y')
    pubmed['title'] = pubmed['title'].str.replace('"','')
    return pubmed



def main(raw_repo,preprocess_repo):
	
	list_of_files = os.listdir(raw_repo)
	list_of_file_object = list(create_file_object(list_of_files,raw_repo))
	dict_ds = load_data (list_of_file_object)

	
	#The main function do the preprocessing necessary in order to clean
	#the datasets from pubmed, clinical_trials and drug raw files.
	

	for category in dict_ds :
		if  category == 'clinicaltrials':

			try:
				preproc_c_trials = preprocess_c_trials(dict_ds[category].dataset)
				write_preprocessed_data(preproc_c_trials,dict_ds[category]
					.name,preprocess_repo,"csv")
			except:
				Preprocessing_logger.error("The preprocessing of clinicaltrials data raise an error")
				raise
		elif category == 'pubmed':
			try:	
				preproc_pubmed = preprocess_pubmed(dict_ds[category].dataset)
				write_preprocessed_data(preproc_pubmed,dict_ds[category]
					.name,preprocess_repo,"csv")
			except:
				Preprocessing_logger.error("The preprocessing of pubmed data raised an error")
				raise
				
	
		else :
			try:
				copy_csv(raw_repo + dict_ds[category].name,preprocess_repo 
					+ dict_ds[category].name)
			except:
				Preprocessing_logger.error("The copy of the raw data with no preprocessing went wrong")
				raise
				