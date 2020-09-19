# -*- coding: utf-8 -*-
"""
Created on Thu Aug 27 13:09:15 2020

@author: xixiu
"""

from os import listdir, path
import cv2 as cv
import numpy as np


# subfolder name
folder_name = './S5C3_JPEG'
# first frame name
first_name = '1589278668825-S5C3.jpeg'
last_name = '1589279085836-S5C3.jpeg'


# extract list of frames of interest
list_jpg = listdir(folder_name)

first_pos = list_jpg.index(first_name);
last_pos = list_jpg.index(last_name);
del list_jpg[last_pos:len(list_jpg)-1]
del list_jpg[0:first_pos]

pyrolysis_front_array = []

from find_informations_of_images import get_pyrolysis_front

for k in range(0, len(list_jpg)-1, 1000):
    img = path.join(folder_name+'/'+list_jpg[k])
    pyrolysis_front_each = get_pyrolysis_front(img)
    pyrolysis_front_array.append(pyrolysis_front_each)
