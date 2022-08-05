import logging
logging.basicConfig(filename='logTask_01',
                    level= logging.INFO,
                    format = '%(levelname)s %(asctime)s %(name)s %(message)s')

logging .info('We will attempt all the tasks in a single file. The task is easier in Jupyter notebook but still.')

import pandas as pd

logging.info('Reading the file: Fitbit_Data.csv')

df = pd.read_csv('D:\iNeuron\dataBase\Fitbit_Data.csv')

logging.info('The Fitbit dataset read into Pycharm.')

logging.info('Q3. convert all the dates avaible in dataset to timestamp format in pandas and in sql you to convert it in date format')

df['ActivityDate'] = pd.to_datetime(df['ActivityDate'])

a = df['ActivityDate'].head()
logging.info(a)

logging.info('Q4. Find out in this data that how many unique ids we have')

logging.info(pd.unique(df['Id']))
logging.info('The number of unique ids is:')
logging.info(len(pd.unique(df['Id'])))

logging.info('Q5 . which id is one of the active id that you have in whole dataset')

'''
There are many ways to count this. One way is the the most calories burnt. 
We will try that.
This data will require us to calculat ethe cummulative value of things.
So we will take a part of data and use it for calculating the cummulative sum.
'''

df1 = df[['Id', 'Calories']]
df1['SumCalories'] = df1.groupby('Id')['Calories'].cumsum()
active = df1.groupby('Id')[['Id','SumCalories']].max()

logging.info('The most active Id and its calories is: ')
logging.info(active[active['SumCalories'] == active['SumCalories'].max()])

logging.info('Q6.how many of them have not logged there activity find out in terms of number of ids.')

''' 
Again we will calculate the cummulative sum of the logged activities.
'''

df1 = df[['Id', 'LoggedActivitiesDistance']]
df1['SumLoggedD'] = df1.groupby('Id')['LoggedActivitiesDistance'].cumsum()
unlogged = df1.groupby('Id')[['Id','SumLoggedD']].max()
logging.info('The Ids which have not logged their activity are: ')
logging.info(unlogged[unlogged['SumLoggedD'] == 0])

logging.info('Q7 . Find out who is the laziest person id that we have in dataset ')

'''
Again we will prepare the same dataset. Laziest person would burn the least amount of calories:
'''

df1 = df[['Id', 'Calories']]
df1['SumCalories'] = df1.groupby('Id')['Calories'].cumsum()
lazy = df1.groupby('Id')[['Id','SumCalories']].max()

logging.info('The most lazy Id and its calories is: ')
logging.info(lazy[lazy['SumCalories'] == lazy['SumCalories'].min()])


logging.info('Q8 . Explore over an internet that how much calories burn is required for a healthy person and find out how many healthy person we have in our dataset')


'''
On an average humans need to burn 2000 Calories. (Considering the average of 1800 for women and 2200 for men).
Therefore, any person/Id who spends > 2000 Calories is healthy.
Its a per day calculation. Many person have good & bad workout day, hence we will calculate the average workout
for each id in this we have to calculate average based on number of days. As the no. of days is different for each id, 
it will be tricky.
'''

logging.info('On an average humans need to burn 2000 Calories. (Considering the average of 1800 for women and 2200 for men).Therefore, any person/Id who spends > 2000 Calories is healthy.')

df1 = df[['Id', 'Calories']]
df1['SumCalories'] = df1.groupby('Id')['Calories'].cumsum()
logging.info('Calculating the value counts of Ids')
# the count of each id could be calculated by
c = df1['Id'].value_counts()

# a dataframe of Id and the final calories counted in the period
e = df1.groupby('Id')[['Id', 'SumCalories']].max()
logging.info('Calculating the average Calories expanded by Ids')
# calculating the average calories of a person per day
e['avg'] = e['SumCalories']/[c[x] for x in e['Id']]

logging.info(e)
# It sees the data is lining up quite nicely
# So will try to see how many persons are buring more than 2000 calories per day
logging.info('The healthy Ids burning more than 2000 calories per day are:')
logging.info(e[e['avg'] >= 2000])

logging.info('Q9.how many person are not a regular person with respect to activity try to find out those')
'''
We can calculate the standard deviation of the activities or distance. Lets calculate the S.D. of Total Distance.
'''

df1 = df.groupby('Id')[['Id', 'TotalDistance']].std()
logging.info(df1)

# Here we can define that any s.d. above 4 km is not a regular person
logging.info('The data of irregular persons are:')
logging.info(df1[df1['TotalDistance'] > 4.0][['TotalDistance']])

logging.info('Q10 Who is the third most active person in this dataset find out those in pandas and in sql both.')

'''
We have calculated the main part of this while calculating the calories sum.
'''

df1 = df[['Id', 'Calories']]
df1['SumCalories'] = df1.groupby('Id')['Calories'].cumsum()
active = df1.groupby('Id')[['Id','SumCalories']].max()

# We will sort the values of the dataset based on SumCalories column and finding its third value
logging.info('The third most active person will be at index 2:')
logging.info(active.sort_values('SumCalories', ascending = False).iloc[2])

logging.info('Q11. who is the 5th most laziest person avilable in dataset find it out')

# We will sort the previous value in ascending order and acess value at index 4
logging.info('The 5th most Laziest person is:')
logging.info(active.sort_values('SumCalories').iloc[4])

logging.info('Q12. what is a totla acumulative calories burn for a person find out')

# We have already calulated this

df1 = df[['Id', 'Calories']]
df1['SumCalories'] = df1.groupby('Id')['Calories'].cumsum()
active = df1.groupby('Id')[['Id','SumCalories']].max()
logging.info(active)


