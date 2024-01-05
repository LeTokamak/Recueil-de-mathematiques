# -*- coding: utf-8 -*-
"""
Created on Tue May  5 22:36:38 2020

@author: Clément
"""

import numpy as np
import matplotlib.pyplot as plt
import math as m

import matplotlib as mpl

from matplotlib.pyplot import cm

fig, ax = plt.subplots(1,1)

# %% Représentation graphique de plusieurs logarithmes

X = np.linspace(0.00001,100,10000)


# %%% Graduations

plt.axhline(y=0, alpha=0.4, color='black')

for i in range(1,10,1):
    plt.axvline(x=i, alpha=0.2, color='black')

for i in range(-2,8):
    plt.axhline(y=i, alpha=0.2, color='black')


# %%% Logarithme décimal et népérien

YLog_10 = []
YLog__e = []

for i in X:
    YLog_10.append(m.log(i,10))
    YLog__e.append(m.log(i,np.e))
    



# %%% Logarithme dans des bases différentes

base_autre = [1.5]

for i in range(80):
    base_autre.append((1.02+0.0005*(i**1.1))*base_autre[-1])

color=iter(cm.rainbow(np.linspace(0,1,len(base_autre))))

for b in base_autre :
    YTemp = []
    for i in X:
        YTemp.append(m.log(i,b))
        
    c=next(color)
    plt.plot(X,YTemp, color = c, alpha= 0.5)



cmap = "rainbow"
norm = mpl.colors.LogNorm(vmin=base_autre[0], vmax=base_autre[-1])

#fig.colorbar(cm.ScalarMappable(norm=norm, cmap=cmap),orientation='vertical', label='Différentes bases de logaritmes')
    

# %%% Echelles et légende

plt.plot(X,YLog_10, color = "blue", linewidth=1.5, label = "Logarithme décimal")
plt.plot(X,YLog__e, color = "red" , linewidth=1.5, label = "Logarithme népérien")

plt.axis([-0.05, 10, -1, 1])
#plt.axis([-0.5, 100, -3, 8])
ax.legend(loc = 4)

plt.show()



# %% Représentation graphique de log_{10} avec les points calculés dans la table
"""

XEx = np.linspace(1,9.9999,899900)
YEx = []
for i in XEx:
    YEx.append(m.log(i,10))
    
plt.plot(XEx,YEx, color = "blue")


XAp = np.array(np.linspace(1,9.9999,8999))
YAp = []
for i in XAp:
    YAp.append(m.log(i,10))

plt.scatter(XAp,YAp, color = "red")

plt.axis([0, 10, 0, 1])

#plt.axis([2.49, 2.51, m.log(2.49,10), m.log(2.51,10)])

for i in range(11):
    plt.axvline(x=i, alpha=0.2, color='black')
    plt.axhline(y=0.1*i, alpha=0.2, color='black')

plt.show()

"""