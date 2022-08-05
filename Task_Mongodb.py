import logging
logging.basicConfig(filename='logTask_Mongodb',
                    level= logging.INFO,
                    format = '%(levelname)s %(asctime)s %(name)s %(message)s')

import pymongo
client = pymongo.MongoClient("mongodb+srv://abhishekMishra:Mongodb894@cluster0.qhvpp.mongodb.net/?retryWrites=true&w=majority")
db = client.test

import pandas as pd
logging.info('Reading the file: Fitbit_Data.csv')

fitbit = pd.read_csv('D:\iNeuron\dataBase\Fitbit_Data.csv')
logging.info('Converting fitbit data to dict format and then inserting it in Mongodb.')

# fitbit = fitbit.to_json()
database = client['Assignment20220731']
collection = database['fitbit']

collection.insert_many(fitbit.to_dict('records'))
logging.info('Fitbit data was inserted in Mongodb\Assignment20220731\fitbit')

'''(logging.info('Reading the Superstore data in Pycharm.')

order = pd.read_excel("D:/iNeuron/dataBase/Superstore_USA.xlsx", sheet_name = 'Orders')
rtr = pd.read_excel("D:/iNeuron/dataBase/Superstore_USA.xlsx", sheet_name = 'Returns')
user = pd.read_excel("D:/iNeuron/dataBase/Superstore_USA.xlsx", sheet_name = 'Users')

logging.info('Converting Order data to json format')

order = order.to_json()

logging.info('Converting Returns data to json format')

rtr = rtr.to_json()

logging.info('Converting Regions & Managers data to json format')

user = user.to_json()

database = client['Assignment20220731']
collection = database['order']
collection.insert_many(order.to_dict('records'))
logging.info('Order data was inserted in Mongodb\Assignment20220731\Order')

database = client['Assignment20220731']
collection = database['return']
collection.insert_many(rtr.to_dict('records'))
logging.info('Return data was inserted in Mongodb\Assignment20220731\return')

database = client['Assignment20220731']
collection = database['Region&Manager']
collection.insert_many(user.to_dict('records'))
logging.info('Regions & Managers data was inserted in Mongodb\Assignment20220731\Region&Manager')

logging.info('Data push to Mongo db completed.'))'''
