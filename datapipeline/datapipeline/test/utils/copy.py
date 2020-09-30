import pandas  as pd
def copy_csv(source,destination):
	pd.read_csv(source).to_csv(destination,index=False)




