import pandas as pd

data= pd.read_csv('transactions.csv')

Data=data[data.STATUS =='OK'].sort_values('SUM', ascending=False).head(3)
print(Data)
