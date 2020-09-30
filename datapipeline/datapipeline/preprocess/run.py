# coding=utf-8
import pandas as pd
import os
import re
from datapipeline.utils.io  import load_data, write_preprocessed_data, create_file_object, file_object
from datapipeline.utils.copy  import copy_csv


raw_repo = 'data/raw/'
preprocess_repo = 'data/preprocess/'
process_repo = 'data/process/'

list_of_files =  os.listdir(raw_repo)



def preprocess_c_trials (clinicalT):
	"""
	This class allow you to store all the main information concerning the raw files
	"""
	clinicalT = clinicalT[clinicalT['scientific_title'].str.strip().map(len)>1].dropna()
	clinicalT_date=pd.to_datetime(clinicalT['date'])
	clinicalT['date'] =  clinicalT_date.dt.strftime('%d/%m/%Y')
	clinicalT['journal'] = clinicalT['journal'].str.replace(r'(\\.*$)','') 
	clinicalT['scientific_title'] = clinicalT['scientific_title'].str.replace(r'(\\.*$)','') 
	return clinicalT

def preprocess_pubmed(pubmed):
	"""
	This class allow you to store all the main information concerning the raw files
	"""
	pubmed = pubmed.drop('id',1)
	pubmed ['id']= pubmed.reset_index().index
	pubmed['date'] =  pd.to_datetime(pubmed['date']).dt.strftime('%d/%m/%Y')
	pubmed['title'] = pubmed['title'].str.replace('"','')
	return pubmed



def main():
	basePath = os.getcwd()
	list_of_file_object = list(create_file_object(list_of_files,raw_repo))
	dict_DS = load_data (list_of_file_object)

	"""
	This function do the preprocessing nécessary in order to clean
	the dataset.
	"""

	for category in dict_DS :
		if  category == 'clinicaltrials':

			try:
				preproc_c_trials = preprocess_c_trials(dict_DS[category].dataset)
				write_preprocessed_data(preproc_c_trials,dict_DS[category].name,preprocess_repo,"csv")
			except:
				print("The preprocessing of clinicaltrials data raise an error")
		elif category == 'pubmed':
			try:	
				preproc_pubmed = preprocess_pubmed(dict_DS[category].dataset)
				write_preprocessed_data(preproc_pubmed,dict_DS[category].name,preprocess_repo,"csv")
			except:
				print("The preprocessing of pubmed data raised an error")
	
		else :
			try:
				copy_csv(raw_repo+dict_DS[category].name,preprocess_repo+dict_DS[category].name)
			except:
				print("The copy of the raw data with no preprocessing went wrong")
				print("An Error was raised")