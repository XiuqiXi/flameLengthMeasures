# -*- coding: utf-8 -*-
"""
Created on Sun Sep 13 10:51:23 2020

@author: xixiu
"""

import numpy as np
from matplotlib import pyplot as plt
import re
from matplotlib import rcParams
import matplotlib.cm as cm
rcParams['font.family']='serif'
rcParams['font.sans-serif']=['Times New Roman']

# font = {'style':'Time New Roman'}

font = {'style':'normal', 'size' : 23}


def movingaverage(interval, window_size):
    window= np.ones(int(window_size))/float(window_size)
    return np.convolve(interval, window, 'same')

t = np.loadtxt('Time.txt')
t_reduce = np.loadtxt('Time_reduce.txt')
t_manual = np.loadtxt('Time_manual.txt')
flame_sum_15 = np.loadtxt('new_flame_sum_15.txt')
flame_sum_30 = np.loadtxt('new_flame_integral_30.txt')
flame_sum_45 = np.loadtxt('new_flame_integral_45.txt')
flame_sum_60 = np.loadtxt('new_flame_integral_60.txt')
flame_manual = np.loadtxt('flame_manual.txt')
edges = np.loadtxt('flame_edges.txt')
ffm = np.loadtxt('data_process/Flame Front Manual_color_image.txt')
flx = np.loadtxt('data_process/Flame Length Existing.txt')

           
# sum_pixels = sum_pixels-edges
# Inte = Inte-edges

from delete_abnormal_data_flame_length import delete_data
flame_sum_15 = delete_data(flame_sum_15)
flame_sum_30 = delete_data(flame_sum_30)
flame_sum_45 = delete_data(flame_sum_45)
flame_sum_60 = delete_data(flame_sum_60)


        
from delete_abnormal_data_flame_length import get_deviation
flame_sum_15_upper, flame_sum_15_lower, flame_sum_15_mean = get_deviation(flame_sum_15)
flame_sum_30_upper, flame_sum_30_lower, flame_sum_30_mean = get_deviation(flame_sum_30)
flame_sum_45_upper, flame_sum_45_lower, flame_sum_45_mean = get_deviation(flame_sum_45)
flame_sum_60_upper, flame_sum_60_lower, flame_sum_60_mean = get_deviation(flame_sum_60)


  
    
# # for k in range(0,len(edges)-10):
# #     if edges[k]>12:
# #         edges[k] = (edges[k-10]+edges[k+10])/2
# edges[0:8000] = 0.332103321
# # edges[0:80] = 0
# # edges = edges-7.9
# plt.figure()
# plt.scatter(flx[:,0],flx[:,1],color ='g', label = 'Existing flame length measures')
# plt.plot(t,edges ,color ='b', label = 'burnout')
# plt.xlim(0, 500)
# # plt.ylim(0, 12)
# plt.legend(loc='upper left')
# plt.xlabel('Time(s)')
# plt.ylabel('Length(mm)')

        
             
f, ax = plt.subplots(1,1)
ax.plot(t, flame_sum_15_mean, color='b', linewidth=2)
ax.fill_between(t, flame_sum_15_lower, flame_sum_15_upper,color='b', alpha=0.2, label = 'sum area threshold 15')

ax.plot(t, flame_sum_30_mean, color='r', linewidth=2)
ax.fill_between(t, flame_sum_30_lower, flame_sum_30_upper,color='r', alpha=0.2, label = 'integral threshold 30')

ax.plot(t, flame_sum_45_mean, color='g', linewidth=2)
ax.fill_between(t, flame_sum_45_lower, flame_sum_45_upper,color='g', alpha=0.2, label = 'threshold 45')

ax.plot(t, flame_sum_60_mean, color='k', linewidth=2)
ax.fill_between(t, flame_sum_60_lower, flame_sum_60_upper,color='k', alpha=0.2, label = 'threshold 60')

# plt.scatter(t_manual,flame_manual*0.332103321,color ='k', label = 'Flame Front Manual')
# plt.scatter(flx[:,0],flx[:,1],color ='g', label = 'Flame Front from Olson')
plt.xlim(0, 500)
plt.ylim(0, 80)
plt.legend(loc='upper left')
plt.xlabel('Time(s)')
plt.ylabel('Length(mm)')

# plt.figure()
# plt.plot(t_reduce,sum_pixels-edges,color ='r', label = 'gamma 1.5 threshold 0.007')
# # plt.scatter(ffm[:,0],ffm[:,1],color ='k', label = 'Flame Front Manual')
# plt.scatter(flx[:,0],flx[:,1],color ='g', label = 'Existing flame length measures')
# plt.legend(loc='upper left')
# plt.ylim(0, 120)
# plt.xlabel('Time(s)')
# plt.ylabel('Area(pixel*pixel)')