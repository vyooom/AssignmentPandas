import logging
logging.basicConfig(filename='logTask_01_MySQL',
                    level= logging.INFO,
                    format = '%(levelname)s %(asctime)s %(name)s %(message)s')

logging.info('The first task in MySQL')

logging.info('Q1: Read the Fitbit Dataset automatically in MySQL.')

logging.info('Using pip & conda I have installed the csv kit.')

logging.info('The command used to create the table dat was:')
logging.info('csvsql -i mysql Fitbit_Data.csv')
logging.info('The output is shown in next line:')

import mysql.connector as connector

db = connector.connect(host = 'localhost', user = 'root', passwd = 'Mysql@894')

cursor = db.cursor()

cursor.execute('create database if not exists Assignment20220731')

logging.info(cursor.fetchall())

q1 = 'CREATE TABLE if not exists Assignment20220731.Fitbit_Data (`Id` DECIMAL(38, 0) NOT NULL,`ActivityDate` DATE NOT NULL,`TotalSteps` DECIMAL(38, 0) NOT NULL,`TotalDistance` DECIMAL(38, 9) NOT NULL,`TrackerDistance` DECIMAL(38, 9) NOT NULL,`LoggedActivitiesDistance` DECIMAL(38, 9) NOT NULL,`VeryActiveDistance` DECIMAL(38, 9) NOT NULL,`ModeratelyActiveDistance` DECIMAL(38, 9) NOT NULL, `LightActiveDistance` DECIMAL(38, 9) NOT NULL,`SedentaryActiveDistance` DECIMAL(38, 9) NOT NULL,`VeryActiveMinutes` DECIMAL(38, 0) NOT NULL,`FairlyActiveMinutes` DECIMAL(38, 0) NOT NULL,`LightlyActiveMinutes` DECIMAL(38, 0) NOT NULL,`SedentaryMinutes` DECIMAL(38, 0) NOT NULL,`Calories` DECIMAL(38, 0) NOT NULL)'

# q1 = 'CREATE TABLE "Fitbit_Data" ("Id" FLOAT NOT NULL, "ActivityDate" DATE NOT NULL, "TotalSteps" FLOAT NOT NULL,"TotalDistance" FLOAT NOT NULL, "TrackerDistance" FLOAT NOT NULL,"LoggedActivitiesDistance" FLOAT NOT NULL,"VeryActiveDistance" FLOAT NOT NULL,"ModeratelyActiveDistance" FLOAT NOT NULL,"LightActiveDistance" FLOAT NOT NULL, "SedentaryActiveDistance" FLOAT NOT NULL,"VeryActiveMinutes" FLOAT NOT NULL,"FairlyActiveMinutes" FLOAT NOT NULL,"LightlyActiveMinutes" FLOAT NOT NULL,"SedentaryMinutes" FLOAT NOT NULL, "Calories" FLOAT NOT NULL)'

logging.info(q1)
cursor.execute(q1)

logging.info('For loading the data directly we will use the command load data infile.')

q2 = "LOAD DATA INFILE 'D:/iNeuron/dataBase/Fitbit.csv' INTO TABLE Assignment20220731.Fitbit_Data FIELDS TERMINATED BY ',' ENCLOSED BY '\t' LINES TERMINATED BY '\n' IGNORE 1 ROWS"

logging.info(q2)

cursor.execute(q2)

logging.info('The Fitbit_data was loaded into MySQL')

db.commit()




