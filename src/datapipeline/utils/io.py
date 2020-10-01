# coding=utf-8
import pandas as pd
import re 
import os


from datetime import datetime

class dataset_object:
    def __init__(self,  dataset,name):
         self.dataset, self.name =  dataset, name



class file_object:
    """
    This class allow you to store all the main information concerning the raw files

    """
    def __init__(self, name, category, extension, path):
        self.name, self.category, self.extension, self.path = name, category, extension, path


def load_data (list_of_file_object):
    dict_ds = {}
    for f in list_of_file_object:
        name_and_ext = re.split(r'\.',f.name)
        if(f.extension == "json"):
            if  f.category in dict_ds:
            	ds =  pd.read_json(f.path + f.name)
            	ds_concat = pd.concat([dict_ds[f.category].dataset,ds])
            	dict_ds[f.category] = dataset_object(ds_concat,name_and_ext[0])
            else:
            	ds = pd.read_json(f.path + f.name)
            	dict_ds[f.category] = dataset_object(ds,name_and_ext[0])
        elif(f.extension == "csv"):
            if  f.category in dict_ds:
            	ds = pd.read_csv(f.path + f.name)
            	ds_concat = pd.concat([dict_ds[f.category].dataset,ds])
            	dict_ds[f.category] = dataset_object(ds_concat,name_and_ext[0])
            else:
            	ds = pd.read_csv(f.path + f.name)
            	dict_ds[f.category] = dataset_object(ds,name_and_ext[0])        
        else:
            dict_ds

    return dict_ds

def create_file_object(list_of_files,repo) :
    """
    This function create from the list of files stored in the repo 
    the corresponding file_object
    """
    
    for e in list_of_files :
        cat_and_ext = re.split(r'\.',e);
        f = file_object(e, re.sub('[^a-zA-Z]+', '',cat_and_ext[0]),
            cat_and_ext[1],repo)
        yield f



def write_preprocessed_data(dataset,file,repo,ext):
    horodate = datetime.now().strftime("%m%d%Y_%H%M%S")

    if not os.path.exists(repo):
        os.makedirs(repo)
        
    if(ext == "csv") :
        dataset.to_csv(repo + file + "_" + horodate + ".csv",index=False)
    else :
        dataset.to_json(repo + file +"_" + horodate + ".json",orient="records")


