import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


data=pd.read_excel('CARGO.xlsx')

graphic_size = data.groupby(data.CARGO).size().to_frame('size').reset_index()
graphic_price = data.groupby(data.CARGO).agg({'PRICE': ['sum']})
graphic_weight = data.groupby(data.CARGO).agg({'WEIGHT': ['sum']})

graphic_size.plot.bar()
plt.show()

graphic_price.plot.bar()
plt.show()

graphic_weight.plot.bar()
plt.show()
