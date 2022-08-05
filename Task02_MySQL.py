import logging
logging.basicConfig(filename='logTask_02_MySQL',
                    level= logging.INFO,
                    format = '%(levelname)s %(asctime)s %(name)s %(message)s')

logging.info('The second task in MySQL')

logging.info('Q1: Read the Superstore Dataset automatically in MySQL.')

logging.info('Using pip & conda I have installed the csv kit.')
import pandas as pd
order = pd.read_excel("D:/iNeuron/dataBase/Superstore_USA.xlsx", sheet_name = 'Orders')
rtr = pd.read_excel("D:/iNeuron/dataBase/Superstore_USA.xlsx", sheet_name = 'Returns')
user = pd.read_excel("D:/iNeuron/dataBase/Superstore_USA.xlsx", sheet_name = 'Users')


logging.info('The command used to create the table data was:')
logging.info('csvsql -i mysql superstore.csv -e 1252')
logging.info('The output is shown in next line:')

