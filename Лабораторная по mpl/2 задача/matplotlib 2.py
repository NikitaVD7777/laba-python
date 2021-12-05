import matplotlib.pyplot as plt
f = open('frames.dat.txt', 'r')
data=[]
for st in f:
    data.append(st)
for i in range(0,len(data),2):
    mas_x = list(map(float, data[i].split()))
    mas_y = list(map(float, data[i + 1].split()))
    plt.plot(mas_x, mas_y)
    plt.title('Frame '+str(i//2))
    plt.grid(color='b', linestyle='-', linewidth=0.5)
    plt.ylim([-10, 12])
    plt.show()



