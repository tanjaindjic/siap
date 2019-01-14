import pip
import json
from vino import Vino
import statistics
import numpy as np
from pprint import pprint
import matplotlib.pyplot as plt
print(pip.__version__)
with open('winemag-data-130k-v2.json') as f:
    data = json.load(f)
print(len(data))
vina = []
for v in data:
    if (v['points'] is not None and v['country'] is not None and v['variety'] is not None and v['title'] is not None):
        vina.append(Vino(v['country'], v['description'], v['points'], v['price'], v['province'], v['taster_name'],  v['title'], v['variety'],  v['winery']))
print(len(vina))
k1=[] #solidan kvalitet vina
k2=[] #vrlo dobar kvalitet vina
k3=[] #izuzetno dobar kvalitet
k4=[] #savrsen kvalitet
for v in vina:
    if(v.price is not None):
        if(int(v.points) < 85):
            k1.append(int(v.price))
        elif(int(v.points) < 90):
            k2.append(int(v.price))
        elif (int(v.points) < 95):
            k3.append(int(v.price))
        else:
            k4.append(int(v.price))
print(len(k1))
print(len(k2))
print(len(k3))
print(len(k4))

prosek_k1 = statistics.median(k1)

print(prosek_k1)
prosek_k2 = statistics.median(k2)
print(prosek_k2)
prosek_k3 = statistics.median(k3)
print(prosek_k3)
prosek_k4 = statistics.median(k4)
print(prosek_k4)
pairs_k1 = []
pairs_k2 = []
pairs_k3 = []
pairs_k4 = []
for v in vina:

    if (v.price is None):
        if (int(v.points) < 85):
            v.price = prosek_k1
            pair = [int(v.price), int(v.points)]
            pairs_k1.append(pair)
        elif (int(v.points) < 90):
            v.price = prosek_k2
            pair = [int(v.price), int(v.points)]
            pairs_k2.append(pair)
        elif (int(v.points) < 95):
            v.price = prosek_k3
            pair = [int(v.price), int(v.points)]
            pairs_k3.append(pair)
        else:
            v.price = prosek_k4
            pair = [int(v.price), int(v.points)]
            pairs_k4.append(pair)
    else:
        if (int(v.points) < 85):
            pair = [int(v.price), int(v.points)]
            pairs_k1.append(pair)
        elif (int(v.points) < 90):
            pair = [int(v.price), int(v.points)]
            pairs_k2.append(pair)
        elif (int(v.points) < 95):
            pair = [int(v.price), int(v.points)]
            pairs_k3.append(pair)
        else:
            pair = [int(v.price), int(v.points)]
            pairs_k4.append(pair)




axes = plt.gca()
axes.set_xlim([0,1000])
a = np.array(pairs_k1)
plt.plot(a[:,0], a[:,1], 'ro')
a = np.array(pairs_k2)
plt.plot(a[:,0], a[:,1], 'mo')
a = np.array(pairs_k3)
plt.plot(a[:,0], a[:,1], 'yo')
a = np.array(pairs_k4)
plt.plot(a[:,0], a[:,1], 'go')
plt.show()
#print(str(vina[0]))
#print(str(vina[1]))