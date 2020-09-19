# -*- coding: utf-8 -*-
"""
Created on Thu Aug 27 14:34:03 2020

@author: xixiu
"""

from os import listdir, path
import cv2 as cv

# def get_the_flame_length(img):
#     img = cv.imread(img)
    
#     img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    
#     img = img[508:708, :]
    
#     # (T, img_substracted) = cv.threshold(img, 35, 255, cv.THRESH_BINARY)
#     img_substracted = cv.Canny(img,30,200)
    
#     for k in range(img_substracted.shape[1]-1, 0, -1):
#         if (sum(img_substracted[:,k]) != 0):
#             break
        
#     return k

# subfolder name
folder_name = './S5C3_JPEG'
# first frame name
# first_name = '1589278668825-S5C3.jpeg'
# last_name = '1589279085836-S5C3.jpeg'

first_name = '1589278577007-S5C3.jpeg'
last_name = '1589279085836-S5C3.jpeg'


# extract list of frames of interest
list_jpg = listdir(folder_name)

first_pos = list_jpg.index(first_name);
last_pos = list_jpg.index(last_name);
del list_jpg[last_pos:len(list_jpg)-1]
del list_jpg[0:first_pos]

flame_length_array = []

from find_informations_of_images import get_pyrolysis_front

number_write = open("flame.txt","w")

for k in range(0, len(list_jpg)-1, 62):
    img = path.join(folder_name+'/'+list_jpg[k])
    flame_length_each = get_pyrolysis_front(img)
    flame_length_array.append(flame_length_each)
    str_flame_length = str(flame_length_each)
    str_flame_length = str_flame_length[1:]
    str_flame_length = str_flame_length[:-1]
    number_write.write(str_flame_length+"\n")

number_write.close()

# img = cv.imread('1589278769816-S5C3.jpeg')

# img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

# img = img[508:708, :]

# (T, img_substracted) = cv.threshold(img, 35, 255, cv.THRESH_BINARY)

# cv.imshow('img', img_substracted)

# for k in range(img_substracted.shape[1]-1, 0, -1):
#     if (sum(img_substracted[:,k]) != 0):
#         break
    