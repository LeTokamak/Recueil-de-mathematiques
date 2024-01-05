# -*- coding: utf-8 -*-
"""
Created on Tue May  5 22:36:38 2020

@author: Clément
"""

import numpy as np
import matplotlib.pyplot as plt
import math as m

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