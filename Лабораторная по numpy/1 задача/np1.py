import numpy as np
from PIL import Image
number='01'
img = Image.open('lunar'+number+'_raw.jpg')
data = np.array(img)

mas_min=[]
mas_max=[]
for i in data:
    mas_min.append(min(i))
    mas_max.append(max(i))

k=round((255/(max(mas_max)-min(mas_min))),1)
b=round((-1)*min(mas_min)*k,1)

for i in range (len(data)):
    for j in range(len(data[i])):
        data[i][j]=int(data[i][j]*k+b)

# запись картинки после обработки
res_img = Image.fromarray(data)
res_img.save('new_lunar'+number+'_raw.jpg')