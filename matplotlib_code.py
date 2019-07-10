# -*- coding: utf-8 -*-
"""
Created on Mon Jul  8 08:45:39 2019

@author: Aromal
"""

import numpy as np
import matplotlib.pyplot as plt

x=np.linspace(0,10,1000)
sines=np.sin(x)
plt.xlabel("x");
plt.ylabel("y")
plt.plot(x,sines,label=('sinx'))
plt.plot(x,np.cos(x),label=('cosx'))
plt.legend(loc="lower right")
plt.show()

_range=np.random.RandomState(5)
y=_range.normal(loc=0,scale=50,size=500)
binsize=np.arange(-100,100,10)
plt.hist(y,bins=binsize)
plt.show()

z=_range.normal(size=500)
plt.scatter(y,z,color=["yellow","lightblue"])
plt.show()