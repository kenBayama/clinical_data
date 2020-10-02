# -*- coding: utf-8 -*-



import logging



"""

Description :

    Configure the loggings with the same logs file, the same format, and the

    same level

Args:

    filename: "../.logs"

    filemode: 'a' (append data to file or create file if not exists)

    format: for eg. 2020/08/21 11:46:36,466 -- PARSING STEP : INFO : App ended parsing the content of profile -> wissam-gherissi-322151163

    datefmt: for eg. 2020/08/21 11:46:36,466

    level: "NOTSET", "DEBUG", "INFO", "WARNING", "ERROR" or "CRITICAL"



Returns:

    output: (logger type object,

             logger type object,

             logger type object,

             logger type object)

"""



logging.basicConfig(filename = "logs/datapipeline.logs",

                    filemode='a',

                    format='%(asctime)s,%(msecs)d -- %(name)s : %(levelname)s : %(message)s',

                    datefmt='%Y/%m/%d %H:%M:%S',

                    level=logging.NOTSET)



# Initialize 4 Loggers

Main_logger = logging.getLogger('OVERALL PROCESSING STEP')

Preprocessing_logger = logging.getLogger('PREPROCESSING STEP')

Processing_logger = logging.getLogger('PROCESSING STEP')


