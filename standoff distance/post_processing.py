# -*- coding: utf-8 -*-
"""
Created on Tue Sep  7 12:50:50 2021

@author: xixiu
"""

import numpy as np
from matplotlib import pyplot as plt
import re
from matplotlib import rcParams
import matplotlib.cm as cm
import scipy.signal as signal

rcParams['font.family']='serif'
rcParams['font.sans-serif']=['Times New Roman']

font = {'style':'normal', 'size' : 23}


standoff = np.loadtxt("standoff.txt")

for i in range(len(standoff)):
    if standoff[i] > 50 and i < 3000:
        standoff[i] = (standoff[i+2]+standoff[i-2])/2
        
for i in range(len(standoff)):
    if standoff[i] > 50 and i < 3000:
        standoff[i] = (standoff[i+2]+standoff[i-2])/2
        
for i in range(len(standoff)):
    if standoff[i] > 50 and i < 3000:
        standoff[i] = (standoff[i+2]+standoff[i-2])/2

for i in range(len(standoff)):
    if standoff[i] > 30 and i < 3000:
        standoff[i] = (standoff[i+2]+standoff[i-2])/2
        
        
standoff = signal.medfilt(standoff,5)
standoff = signal.medfilt(standoff,5)


plt.figure()
plt.plot(np.linspace(18.4, 541, len(standoff)),standoff,color ='midnightblue')
plt.xlabel('Time(s)')
plt.ylabel('Distance(pixels)')