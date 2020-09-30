# coding=utf-8
import pandas  as pd
from datetime import datetime



def copy_csv(source,destination):
	horodate = datetime.now().strftime("%m%d%Y_%H%M%S")
	pd.read_csv(source + ".csv").to_csv(destination 
		+ "_" + horodate + ".csv",index=False)

def copy_json(source,destination):
	horodate = datetime.now().strftime("%m%d%Y_%H%M%S")
	pd.read_json(source + ".json").to_json(destination
		+ "_" + horodate + ".csv",index=False)

