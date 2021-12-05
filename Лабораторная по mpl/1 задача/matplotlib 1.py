import matplotlib.pyplot as plt

f = open('001.txt', 'r')
mas_x=[]
mas_y=[]
for st in f :
    st_coor=list(map(float,st.split()))
    mas_x.append(st_coor[0])
    if(len(st_coor)>1):
        mas_y.append(st_coor[1])
mas_x.pop(0)

plt.plot(mas_x, mas_y,'ro')
plt.show()

