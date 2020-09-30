import pandas as pd
def load_data (list_of_tuple_file):
	list_dataset = List()
	for tuple_file in list_of_tuple_file:
		source,extension = tuple_file
		if(extension == "json"):
			list_dataset.append(pd.read_json(source))
		elif(extension == "csv"):
			list_dataset.append(pd.read_json(source))
		else:
			list_dataset

	return list_dataset


def write_preprocessed_data(dataset,name,path):
	horodate = datetime.now().strftime("%m%d%Y_%H%M%S")
	#dataset.to_csv(path+name+'_'+horodate".csv",index=False)
