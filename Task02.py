import logging
logging.basicConfig(filename='logTask_02',
                    level= logging.INFO,
                    format = '%(levelname)s %(asctime)s %(name)s %(message)s')

logging .info('We will attempt all the tasks in a single file. The task is easier in Jupyter notebook but still.')

logging.info('Importing the super store data. The three different sheets to be read.')

import pandas as pd
order = pd.read_excel("D:/iNeuron/dataBase/Superstore_USA.xlsx", sheet_name = 'Orders')
rtr = pd.read_excel("D:/iNeuron/dataBase/Superstore_USA.xlsx", sheet_name = 'Returns')
user = pd.read_excel("D:/iNeuron/dataBase/Superstore_USA.xlsx", sheet_name = 'Users')

logging.info('The sheets Orders, Return & Users read in PyCharm.')

logging.info('Q3. Find out how many return that we ahve recived and with a product id')

logging.info('We have received %s number of returns.'%len(rtr['Order ID']))

logging.info('For product ids we have to join return with Row id in Order')

a = pd.merge(rtr['Order ID'], order[['Row ID', 'Order ID']], on = 'Order ID', how = 'left')
logging.info(a.head())

logging.info('Q4 . try  to join order and return data both in sql and pandas')

b = pd.merge(order, rtr, on = 'Order ID', how = 'inner')
logging.info(b.head())

logging.info('5 . Try to find out how many unique customer that we have')
a = pd.unique(order['Customer ID'])
logging.info('The number of unique customers are: %s'%s(len(a)))

logging.info('Q6.try to find out in how many regions we are selling a product and who is a manager for a respective region')

# This data is avialble in 'User Sheet'.
reg = pd.unique(order['Region'])

logging.info('The number of unique regions in order are: %s'%reg)

for i in reg:
    m = user[user['Region'] == i]
    logging.info(m)

logging.info('Q7 . find out how many different differnet shipement mode that we have and what is a percentage usablity of all the shipment mode with respect to dataset')

shipMode = pd.unique(order['Ship Mode'])
logging.info('There are %s types of shipping modes and they are: %s'%(len(shipMode), shipMode))

# we can use normalize as true for the value counts to get the porpotion of data
logging.info(order['Ship Mode'].value_counts(normalize = True))

#8 . Create a new coulmn and try to find our a diffrence between order date and shipment date
order['Pickup'] = order['Ship Date'] - order['Order Date']
logging.info(order['Pickup'].head())

logging.info('Q9 . base on question number 8 find out for which order id we have shipment duration more than 10 days')

# we have to use the datetime package

import datetime

logging.info(order[order['Pickup'] > datetime.timedelta(days = 10)][['Order ID', 'Pickup']])

logging.info('Q10. Try to find out a list of a returned order which shipment duration was more then 15 days and find out that region manager as well ')

import datetime

d1 = order[order['Pickup'] > datetime.timedelta(days = 15)][['Order ID', 'Region', 'Pickup']]
d2 = pd.merge(d1, rtr, on = 'Order ID', how = 'left')
d3 = pd.merge(d2, user, on = 'Region', how = 'left')

logging.info('The return orders with shipment more than 15 days are:')
logging.info(d3)

logging.info('Q11 . Group by region and find out which region is more profitable')
a = order.groupby('Region', as_index = False)[['Region','Profit']].sum()
logging.info(a)
logging.info('The region with highest profit is:')
logging.info(a[a['Profit'] == a['Profit'].max()])

logging.info('Q12 . Try to find out overalll in which country we are giving more discount')

# there is no country as such we can sort on States

a = order.groupby('State or Province', as_index = False)['Discount'].sum()
logging.info(a[a['Discount'] == a['Discount'].max()])

logging.info('Q13 . Give me a list of unique postal code ')

d = list(pd.unique(order['Postal Code']))
logging.info(d)

logging.info('Q14 . which customer segement is more profitalble find it out.')

a = order.groupby('Customer Segment', as_index = False)['Profit'].sum()

logging.info(a[a['Profit'] == a['Profit'].max()])

logging.info('Q15. try to find out the 10th most loss making product catagory.')
loss = order.groupby('Product Category', as_index = False)['Profit'].sum()
# As it has only three categories, we will check
loss = order.groupby('Product Sub-Category', as_index = False)['Profit'].sum()
logging.info(loss.sort_values('Profit').iloc[9])

logging.info('Q16 . Try to find out 10 top  product with highest margins')

margin = order.groupby('Product Name', as_index = False)['Product Base Margin'].sum()
logging.info(margin.sort_values('Product Base Margin', ascending = False).iloc[0:10])




