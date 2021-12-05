import pandas as pd

data1 = pd.read_excel('123.xlsx')
data2 = pd.read_excel('students_info.xlsx')

data = pd.merge(data1, data2, on='login')[(data1.G >9) | (data1.H >9)]

print(data)


