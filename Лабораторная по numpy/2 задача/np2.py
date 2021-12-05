import numpy as np
import matplotlib.pyplot as plt

data = np.loadtxt("signal03.txt")
alpha=[i for i in range(len(data))]
plt.plot(alpha, data)
plt.title('Сырой сигнал')
plt.grid(color='b', linestyle='-', linewidth=0.5)
plt.show()

for i in range(1,len(data)):
    if(i<10):
        data[i]=(sum(data[0:i+1]))/(i+1)
        # print(data[:i])
    else:
        data[i]=(sum(data[i-9:i+1]))/10

plt.plot(alpha, data)
plt.title('После фильтра')
plt.grid(color='b', linestyle='-', linewidth=0.5)
plt.show()
