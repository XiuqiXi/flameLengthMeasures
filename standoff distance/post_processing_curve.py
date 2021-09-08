# -*- coding: utf-8 -*-
"""
Created on Wed Sep  8 01:10:11 2021

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


curve_fitting_para = np.loadtxt("curve_fiting.txt")

time_index = curve_fitting_para[:,0]
time = time_index/(15577/(541-18.4))+18.4
time[10300] = (time[10301]+time[10299])/2
para = curve_fitting_para[:,1]
std = curve_fitting_para[:,2]

for i in range(len(time)):
    if para[i] > 2.1 and time[i] < 200:
        para[i] = (para[i+2]+para[i-2])/2
        
for i in range(len(time)-5):
    if para[i] > 5:
        para[i] = (para[i+2]+para[i-2])/2
        
for i in range(len(time)-5):
    if para[i] > 5:
        para[i] = (para[i+2]+para[i-2])/2
        
for i in range(len(time)-5):
    if para[i] > 5:
        para[i] = (para[i+2]+para[i-2])/2
        
para = signal.medfilt(para,5)
para = signal.medfilt(para,5)

plt.figure()
plt.plot(time,para,color ='midnightblue')
plt.xlabel('Time(s)')
plt.ylabel('Fitting coefficient')

plt.figure()
plt.scatter(time,std,color ='midnightblue', s=1)
plt.ylim(0,1)
plt.xlabel('Time(s)')
plt.ylabel('R-square')

