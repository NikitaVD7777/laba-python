import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('kr.csv', sep=";", header= None)
df.columns = ['prep','group', 'marks']
prep_sorted = df.groupby(['prep', 'marks'])['prep'].count().unstack('marks').fillna(0)
group_sorted = df.groupby(['group', 'marks'])['group'].count().unstack('marks').fillna(0)
prep_sorted.plot(kind='bar', stacked=True, rot= 0)
group_sorted.plot(kind='bar', stacked=True, rot= 0)
plt.show()