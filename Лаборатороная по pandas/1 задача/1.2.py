import pandas as pd

data= pd.read_csv('transactions.csv')
Data= data[(data.STATUS == 'OK') & (data.CONTRACTOR == 'Umbrella, Inc')].agg({'SUM': ['sum']})
print(Data)
