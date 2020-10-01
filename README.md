This Project is a project of a Data Pipeline processing semi structured data from pharmaceutical input.


### Environnement ###
Python3.8

Check the requirement file to know what need to be installed apart from python.


### Project Structure ###
datapipeline/&nbsp;&nbsp;&nbsp;&nbsp;Root&nbsp;project&nbsp;directory
├──&nbsp;docs/&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Documentation&nbsp;(.md/.rst&nbsp;files)
├──&nbsp;conf/&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;	Config&nbsp;files&nbsp;(.yml)
├──&nbsp;logs/&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Logfiles
├──&nbsp;notebooks/&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;EDA&nbsp;and&nbsp;validation&nbsp;(.ipynb)
├──&nbsp;scripts/&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Deployment,&nbsp;Dockerfile,&nbsp;etc.
├──&nbsp;data/
│&nbsp;&nbsp;&nbsp;├──&nbsp;raw/&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Raw&nbsp;Data
│&nbsp;&nbsp;&nbsp;├──&nbsp;preprocess/&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Preprocessed&nbsp;Data
│&nbsp;&nbsp;&nbsp;├──&nbsp;process/&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;				Processed&nbsp;Data
│&nbsp;&nbsp;&nbsp;├──&nbsp;result_sample/&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;			An&nbsp;Example&nbsp;of&nbsp;the&nbsp;results
│&nbsp;&nbsp;&nbsp;├──&nbsp;test/&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;					An&nbsp;Example&nbsp;of&nbsp;the&nbsp;results
│&nbsp;&nbsp;&nbsp;│&nbsp;&nbsp;&nbsp;├──&nbsp;raw&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;	preprocess,&nbsp;model.&nbsp;
│&nbsp;&nbsp;&nbsp;│&nbsp;&nbsp;&nbsp;├──&nbsp;preprocess
│&nbsp;&nbsp;&nbsp;│&nbsp;&nbsp;&nbsp;├──&nbsp;process
│&nbsp;&nbsp;&nbsp;│&nbsp;&nbsp;&nbsp;└──&nbsp;result_sample
├──&nbsp;env/&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;	Virtual&nbsp;env,&nbsp;add&nbsp;to&nbsp;.gitignore
├──&nbsp;datapipeline/&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Top&nbsp;level&nbsp;package&nbsp;dir
│&nbsp;&nbsp;&nbsp;├──&nbsp;preprocess/&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Preprocessing&nbsp;(.py,&nbsp;not&nbsp;shown)
│&nbsp;&nbsp;&nbsp;├──&nbsp;process/&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Processing&nbsp;(.py)
│&nbsp;&nbsp;&nbsp;├──&nbsp;utils/&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Util&nbsp;functions&nbsp;used&nbsp;in&nbsp;source,
│&nbsp;&nbsp;&nbsp;│&nbsp;&nbsp;&nbsp;├──&nbsp;__init__.py&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
│&nbsp;&nbsp;&nbsp;│&nbsp;&nbsp;&nbsp;├──&nbsp;copy.py&nbsp;					
│&nbsp;&nbsp;&nbsp;│&nbsp;&nbsp;&nbsp;└──&nbsp;io.py
│&nbsp;&nbsp;&nbsp;├──&nbsp;test/&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;	Test&nbsp;py&nbsp;files
│&nbsp;&nbsp;&nbsp;│&nbsp;&nbsp;&nbsp;├──&nbsp;preprocess/
│&nbsp;&nbsp;&nbsp;│&nbsp;&nbsp;&nbsp;├──&nbsp;process/
│&nbsp;&nbsp;&nbsp;│&nbsp;&nbsp;&nbsp;├──&nbsp;utils/
│&nbsp;&nbsp;&nbsp;│&nbsp;&nbsp;&nbsp;│&nbsp;&nbsp;&nbsp;├──&nbsp;__init__.py
│&nbsp;&nbsp;&nbsp;│&nbsp;&nbsp;&nbsp;│&nbsp;&nbsp;&nbsp;├──&nbsp;copy.py
│&nbsp;&nbsp;&nbsp;│&nbsp;&nbsp;&nbsp;│&nbsp;&nbsp;&nbsp;└──&nbsp;io.py
│&nbsp;&nbsp;&nbsp;│&nbsp;&nbsp;&nbsp;└──&nbsp;__init__.py
│&nbsp;&nbsp;&nbsp;├──&nbsp;__main__.py&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Package&nbsp;execution&nbsp;entry&nbsp;point:
│&nbsp;&nbsp;&nbsp;├──&nbsp;__init__.py&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"python&nbsp;-m&nbsp;datapipeline"
│&nbsp;&nbsp;&nbsp;└──&nbsp;run.py&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Called&nbsp;from&nbsp;__main__.py
├──&nbsp;README.md&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Intro&nbsp;to&nbsp;package
├──&nbsp;setup.py&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Installing&nbsp;the&nbsp;package
├──&nbsp;requirements.txt&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Lists&nbsp;dependencies
└──&nbsp;LICENSE.md&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
</blockquote>&nbsp;&nbsp;

### Lauch the project ###


-	install and create a virtual environment :

			pip install virtualenv
			python3 -m venv env
			.\env\Scripts\activate

-	Install the required environnment project :
	
			pip install -r requirements.txt

	

-	from the datapipeline repo :

			cd src

-	Lauch the preprocess stage :
		
			python -m datapipeline --task preprocess

The preprocess stage allow you to preprocess and clean :


 the data from the data/raw repo and stored the result in the data/preprocess repo

-	Lauch the process stage :

			python -m datapipeline --task process

The process stage allow you to transform the cleaned data into a bond graph which is represented throught four differents files linked through there foreign keys :
  pubmed.json, clinical_trials.json, drug.json, journal.json

Data Model : 

journal.json :
	
	id => primary key
 	atccode => foreign key
 	journal
 	date

drug.json :
	
	atccode => primary key
	clinical_trials_id => foreign key
	pubmed_id => foreign key
	journal_id => foreign key
	drug


clinical_trials.json : 
	
	id => primary key
	atccode => foreign key
	scientific_title
	date
	journal

pubmed.json :
	
	id => Primary key 
	atccode => foreign Key
	title
	date
	journal

#### Improvement => "Pour Aller Plus loin" ###

Storing the data in a PostgreSql database et with SqlAlchemy to produce one file that represent properly the graph bond.

Implements more generators in the code for better performance and scalability.

Create a configuration file which store all the path et allows to get the test path or the production path automatically by using the python_box

Improve de configurability of most of the parameters

Create logs files for debug

Implement the proper units tests and not only a test environnement

Implement better try except for a better readbility and debugging

