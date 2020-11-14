# -*- coding: utf-8 -*-
"""
Created on Mon Aug 10 09:45:23 2020

@author: xixiu
"""

import os
from os import listdir, path
import cv2 as cv
import numpy as np


# subfolder name
folder_name = './S4C3_JPEG'
# first frame name
# first_name = '1589278668825-S5C3.jpeg'
# last_name = '1589279085836-S5C3.jpeg'

# first_name = '1589278577007-S5C3.jpeg'
# last_name = '1589279098850-S5C3.jpeg'


# extract list of frames of interest
list_jpg = listdir(folder_name)

# first_pos = list_jpg.index(first_name);
# last_pos = list_jpg.index(last_name);
# del list_jpg[last_pos:len(list_jpg)-1]
# del list_jpg[0:first_pos]


# img = cv.imread('./S5C4_JPEG/1589278577436-S5C4.jpeg')
# cv.imshow("img",img)

flame_length_array = []
flame_edges_array = []

# from flame_length_measure_sum_pixels import flame_length_measure
from flame_length import flame_length_measure
# from flame_edges import flame_edges_measure_sum
# from flame_edges import flame_edges_measure

number_write = open("burnoutLocation.txt","w")

a = 0
time = np.linspace(0, 166.6, 4998)
for k in range(0, len(list_jpg)-1, 1):
    img = path.join(folder_name+'/'+list_jpg[k])
    # if time[k]<100:
    #     threshold = 15
    # elif (time[k]>100 and time[k]<300):
    #     threshold = 20
    # elif (time[k]>300 and time[k]<400):
    #     threshold = 25
    # elif (time[k]>400 and time[k]<4450):
    #     threshold = 20
    # elif time[k]>450:
    #     threshold = 15
        
    flame_length_each = flame_length_measure(img, 50)
    flame_length_array.append(flame_length_each)
    str_flame_length = str(flame_length_each)
    # str_flame_length = str_flame_length[1:]
    # str_flame_length = str_flame_length[:-1]
    number_write.write(str_flame_length+"\n")
    a = a+1
    b = len(list_jpg) - a
    print(b)
    
number_write.close()

# number_write = open("flame_edges_mean.txt","w")

# a = 0

# for k in range(0, len(list_jpg)-1, 1):
#     img = path.join(folder_name+'/'+list_jpg[k])
#     flame_edges_each = flame_edges_measure_sum(img)
#     flame_edges_array.append(flame_edges_each)
#     str_edges_length = str(flame_edges_each)
#     # str_flame_length = str_flame_length[1:]
#     # str_flame_length = str_flame_length[:-1]
#     number_write.write(str_edges_length+"\n")
#     a = a+1
#     b = len(list_jpg) - a
#     print(b)
    
# number_write.close()

# fps = 30
# size=(1216,1500)
# # fourcc = cv.VideoWriter_fourcc('P', 'I', 'M', 'I')
# fourcc = cv.VideoWriter_fourcc(*'XVID')
# videoWriter = cv.VideoWriter('flame_length.avi',fourcc,fps,size)
# a = 0
    
# time = np.linspace(0, 156.667, 4700)
# for k in range(0, len(list_jpg)-1, 1):
#     img = path.join(folder_name+'/'+list_jpg[k])
#     img_orig = cv.imread(img)
#     flame_length_each = flame_length_measure(img, 10)
#     cv.imwrite('T.jpg',flame_length_each)
#     img_theshold = cv.imread('T.jpg')
#     time_point = time[k]
#     cv.putText(img_theshold,str(time_point), (400,300), cv.FONT_HERSHEY_SIMPLEX, 0.7,(0,0,255), 1, cv.LINE_AA)
#     videoWriter.write(img_theshold)
#     a = a+1
#     b = len(list_jpg) - a
#     print(b)

# videoWriter.release()


number_write = open("Time.txt","w")

a = 0

for k in np.linspace(0, 166.6, 4998):
    k = str(k)
    # str_flame_length = str_flame_length[1:]
    # str_flame_length = str_flame_length[:-1]
    number_write.write(k+"\n")
    a = a+1
    print(a)
    
number_write.close()

%varexp --plot flame_length_array