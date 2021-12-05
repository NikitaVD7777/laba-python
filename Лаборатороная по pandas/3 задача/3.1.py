import pandas as pd
import matplotlib.pyplot as plt

data1 = pd.read_excel('123.xlsx')
data2 = pd.read_excel('students_info.xlsx')

data_group_st = pd.merge(data1, data2, on='login').groupby(data2.group_faculty).agg({'Solved':['mean']})
data_group_it = pd.merge(data1, data2, on='login').groupby(data2.group_out).agg({'Solved':['mean']})

data_group_st.plot.bar()
plt.show()

data_group_it.plot.bar()
plt.show()
