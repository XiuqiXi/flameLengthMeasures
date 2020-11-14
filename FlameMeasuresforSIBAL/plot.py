# -*- coding: utf-8 -*-
"""
Created on Sun Oct 18 19:58:51 2020

@author: xixiu
"""
import numpy as np
from matplotlib import pyplot as plt
from matplotlib import rcParams
rcParams['font.family']='serif'
rcParams['font.sans-serif']=['Times New Roman']

f_t = 'Time.txt'
f_flame_length_10 = 'flameLength.txt'
f_burnout = 'burnoutLocation.txt'
f_flame_length_exist = 'flame_length_exist.txt'
f_flame_length_20 = 'flameLength_20.txt'
f_burnoutExist = 'burnoutExist.txt'


t = np.loadtxt(f_t)
flame_length_10 = np.loadtxt(f_flame_length_10)
flame_length_20 = np.loadtxt(f_flame_length_20)
burnout = np.loadtxt(f_burnout)
flame_length_exist = np.loadtxt(f_flame_length_exist)
burnoutExist = np.loadtxt(f_burnoutExist)

for m in range(5):
    for i in range(len(flame_length_10)-1):
        if (t[i]<124):
            if(flame_length_10[i]>480):
                flame_length_10[i] = (flame_length_10[i-6]+flame_length_10[i+6])/2
                
    for k in range(0,len(flame_length_10)-10):
        if flame_length_10[k]>1.02*(flame_length_10[k-20]+flame_length_10[k+10])/2:
            flame_length_10[k] = (flame_length_10[k-20]+flame_length_10[k+10])/2
            
    for i in range(len(flame_length_20)-1):
        if (t[i]<124):
            if(flame_length_20[i]>480):
                flame_length_20[i] = (flame_length_20[i-6]+flame_length_20[i+6])/2
                
    for k in range(0,len(flame_length_20)-10):
        if flame_length_20[k]>1.02*(flame_length_20[k-20]+flame_length_20[k+10])/2:
            flame_length_20[k] = (flame_length_20[k-20]+flame_length_20[k+10])/2

for i in range(len(burnout)-1):
    if (t[i]<80):
        if(burnout[i]>300):
            burnout[i] = (burnout[i-6]+burnout[i+6])/2
    if (t[i]>13):
        if(burnout[i]<15):
            burnout[i] = (burnout[i-6]+burnout[i+6])/2

for m in range(5):
    for k in range(0,len(burnout)-10):
        if burnout[k]>1.02*(burnout[k-10]+burnout[k+10])/2:
            burnout[k] = (burnout[k-10]+burnout[k+10])/2
    for k in range(0,len(burnout)-10):
        if burnout[k]<1.02*(burnout[k-10]+burnout[k+10])/2:
            burnout[k] = (burnout[k-10]+burnout[k+10])/2


f, ax = plt.subplots(1,1)
ax.plot(np.linspace(0, 144, 4800), flame_length_10[0:4800]-burnout[0:4800], label = 'flame trailing edge overestimation')
ax.plot(np.linspace(0, 144, 4800), flame_length_20[0:4800]-burnout[0:4800], label = 'flame trailing edge underestimation')
# plt.plot(np.linspace(0, 144, 4800), burnout[0:4800], label = 'burnout')
ax.set_xlabel('Time(s)')
ax.set_ylabel('flame trailing edge(mm)')
ax.set_ylim(-25,200)
ax.legend(loc='upper right')
left, bottom, width, height = 0.35,0.58,0.25,0.25
ax2 = f.add_axes([left,bottom,width,height])
ax2.plot(np.linspace(0, 144, 4800), burnout[0:4800],'k')
ax2.set_xlabel('Time(s)')
ax2.set_ylabel('Length(mm)')
ax2.set_title('burnout location')
# ax2.set_xlim(0, 540)
# ax2.set_ylim(0, 6)
# plt.scatter(flame_length_exist[:,0],flame_length_exist[:,1],color ='k', label = 'Flame Front Manual')
# plt.scatter(burnoutExist[:,0],burnoutExist[:,1],color ='b', label = 'Flame Front Sandry')


