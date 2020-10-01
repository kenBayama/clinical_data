This Project is a project of a Data Pipeline processing semi structured data from pharmaceutical input.


### Environnement ###
Python3.8

Check the requirement file to know what need to be installed apart from python.


### Project Structure 
```
├── SQL/                                Repository with the two SQL request
├── src/                                Contain all the source and the sample
│	├── docs/                           Documentation (.md/.rst files)
│	├── logs/                           Logfiles
│	├── data/
│	│   ├── raw/                        Raw Data
│	│   ├── preprocess/                 Preprocessed Data. "Is created when you lauch the preprocess task"
│	│   ├── process/                    Processed Data. "Is created when you lauch the process task"
│	│   ├── result_sample/              Example of the results
│	│   ├── test/                       Result from the testing environment
│	│   │   ├── raw                     
│	│   │   ├── preprocess
│	│   │   ├── process
│	│   │   └── result_sample
│	└── datapipeline/                   Top level package dir
│	    ├── preprocess/                 Preprocessing (.py)
│	    ├── process/                    Processing (.py)
│	    ├── utils/                      Util functions used in source,
│	    │   ├── __init__.py              
│	    │   ├── copy.py
│	    │   └── io.py
│	    ├── test/                       Testing environment
│	    │   ├── preprocess/
│	    │   ├── process/
│	    │   ├── utils/
│	    │   │   ├── __init__.py
│	    │   │   ├── copy.py
│	    │   │   └── io.py
│	    │   └── __init__.py
│	    ├── __main__.py                 Package execution entry point:
│	    ├── __init__.py                 "python -m datapipeline"
│       └── run.py                      Called from __main__.py
├── README.md                       Intro to package
├── requirements.txt                Lists dependencies
└── LICENSE.md
```


### Lauch the project #


-	Install and create a virtual environment :

			pip install virtualenv
			python3 -m venv env
			.\env\Scripts\activate

-	Install the required environnment for the project :
	
			pip install -r requirements.txt

	

-	From the src repo :

			cd src


-	Lauch **the preprocess stage** :
		
			python -m datapipeline --task preprocess



***The preprocess stage allow you to preprocess and clean*** :

The data is loaded from the data/raw repo
There are three categories of data and just two required:

#### pubmed 
Concerning the pubmed files, the following cleaning are done   :

	            Removing the space in the beguinning and the end of the scientific_title column
	            Dropping the row with NaN data in it
	            Converting the date column into a panda datetime column
	            Formatting the datetime column to have the same format for each column
	            Cleaning the journal column to remove hexadecimal characters
	            Cleaning the  journal column to remove hexadecimal characters 

#### clinicals_trials
Concerning the clinical_trials files, the folowwing preprocessing are done :

	            Removing the wrong id and setting a proper one
	            Formatting the datetime column to have the same format for each column
	            Cleaning the title column by removing unnecessary double quote chracter

#### drugs

	           No cleaning required. 

 		

 -	The result are stored in the data/preprocess repo


-	Lauch **the process stage** :

			python -m datapipeline --task process


***The process stage allow you to transform the cleaned data into a bond graph which is represented throught three differents files linked through there foreign keys to one file, drug.json :***

* pubmed.json
* clinical_trials.json
* drug.json
* journal.json

To get to this result the following processing stages were required :

#### Preparation:

		Storing all relevant informationa about each files in a class of object called a file_object
		Loading the data and stored them in dictionary of elment of the class dataset_object which contains the data and the category of that data
		Creating a dictionary with the drug name as key and the atccode as value

#### Processing First Stage: 

-	Processing the data from clinical_trials and pubmed sources by :

		Finding the drugs name in each scientic title or title column
		Turning every letter in uppercase for latter use
		Renaming the date column
		Producing new dataset from clinicals_trials and pubmed

#### Processing Second Stage:

-	Creating the journal data from the new dataset from clinicals_client and pubmed by :

        Keeping only the journal, date_mention and atccode column
        Joining the two dataframe.
        Turning every letter to uppercase
        Grouping by the column journal
        Aggregating by concatenation of string 
        Cleaning by using the clean_column function
        Creating an Index


***Data Model :*** 


drug.json :
	
	atccode > primary key
	drug


journal.json :

	id > primary key
	atccode > foreign key
	journal
	date


clinical_trials.json : 
	
	id > primary key
	atccode > foreign key
	scientific_title
	date
	journal

pubmed.json :
	
	id > Primary key 
	atccode > foreign Key
	title
	date
	journal

### Improvement => "Pour aller plus loin" ###


-	Storing the data in a PostgreSql database et with SqlAlchemy to produce one file that represent properly the graph bond.

-	Implements more generators in the code for better performance and scalability.

-	Create a configuration file which store all the path and allows to get the test path or the production path automatically by using the python_box

-	Improve de configurability of most of the parameters

-	Create logs files for debug

-	Implement the proper units tests and not only a test environnement

-	Implement better try except for a better readbility and debugging

