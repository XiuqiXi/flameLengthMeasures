# -*- coding: utf-8 -*-
"""
Created on Tue Sep  7 11:39:27 2021

@author: xixiu
"""

import os
from os import listdir, path
import cv2 as cv
import numpy as np
from trailing_edge import stand_off


# subfolder name
folder_name = './S5C4_JPEG'
# first frame name
# first_name = '1589278668825-S5C3.jpeg'
# last_name = '1589279085836-S5C3.jpeg'

first_name = '1589278577036-S5C4.jpeg'
last_name = '1589279098842-S5C4.jpeg'


# extract list of frames of interest
list_jpg = listdir(folder_name)

first_pos = list_jpg.index(first_name);
last_pos = list_jpg.index(last_name);
del list_jpg[last_pos:len(list_jpg)-1]
del list_jpg[0:first_pos]


flame_standoff = []
std = []

number_write = open("curve_fiting.txt","w")

a = 0
time = np.linspace(18.4, 541, 15577)
for k in range(200, len(list_jpg)-1, 1):
    try:
        img = path.join(folder_name+'/'+list_jpg[k])
           
        flame_standoff_each, std_each = stand_off(img)
        flame_standoff.append(flame_standoff_each)
        std.append(std_each)
        str_flame_length = str(flame_standoff_each)
        str_std = str(std_each)
        # str_flame_length = str_flame_length[1:]
        # str_flame_length = str_flame_length[:-1]
        number_write.write(str(k) + " " + str_flame_length + " " + str_std +"\n")
    except:
        print("error")
    finally:
        a = a+1
        b = len(list_jpg) - a
        print(b)
    
number_write.close()