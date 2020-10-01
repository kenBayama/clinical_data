This Project is a project of a Data Pipeline processing semi structured data from pharmaceutical input.


### Environnement ###
Python3.8

Check the requirement file to know what need to be installed apart from python.


### Project Structure 

datapipeline/						Root project directory
├── docs/                           Documentation (.md/.rst files)
├── conf/                        	Config files (.yml)
├── logs/                           Logfiles
├── notebooks/                      EDA and validation (.ipynb)
├── scripts/                        Deployment, Dockerfile, etc.
├── data/
│   ├── raw/                        Raw Data
│   ├── preprocess/                 Preprocessed Data
│   ├── process/     				Processed Data
│   ├── result_sample/     			An Example of the results
│   ├── test/     					An Example of the results
│   │   ├── raw                	preprocess, model. 
│   │   ├── preprocess
│   │   ├── process
│   │   └── result_sample
├── env/                         	Virtual env, add to .gitignore
├── datapipeline/                   Top level package dir
│   ├── preprocess/                 Preprocessing (.py, not shown)
│   ├── process/                    Processing (.py)
│   ├── utils/                      Util functions used in source,
│   │   ├── __init__.py              
│   │   ├── copy.py 					
│   │   └── io.py
│   ├── test/                     	Test py files
│   │   ├── preprocess/
│   │   ├── process/
│   │   ├── utils/
│   │   │   ├── __init__.py
│   │   │   ├── copy.py
│   │   │   └── io.py
│   │   └── __init__.py
│   ├── __main__.py                 Package execution entry point:
│   ├── __init__.py                 "python -m datapipeline"
│   └── run.py                      Called from __main__.py
├── README.md                       Intro to package
├── setup.py                        Installing the package
├── requirements.txt                Lists dependencies
└── LICENSE.md         

.
├── build                   # Compiled files (alternatively `dist`)
├── docs                    # Documentation files (alternatively `doc`)
├── src                     # Source files (alternatively `lib` or `app`)
├── test                    # Automated tests (alternatively `spec` or `tests`)
├── tools                   # Tools and utilities
├── LICENSE
└── README.md

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

