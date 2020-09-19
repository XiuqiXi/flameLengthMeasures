# -*- coding: utf-8 -*-
"""
Created on Wed Aug  5 22:42:25 2020

@author: xixiuqi
"""

from os import listdir, path
import numpy as np


# subfolder name
folder_name = './S5C3_JPEG'
# first frame name
first_name = '1589278577207-S5C3.jpeg'


# extract list of frames of interest
list_jpg = listdir(folder_name)

# first frame of interest, remove previous frames from list_jpg
first_pos = list_jpg.index(first_name)
del list_jpg[0:first_pos]

# Extract time from frame name (use last 7 digits)
timestamp = np.zeros(np.size(list_jpg))
for k in range(0,np.size(list_jpg)):
    timestamp[k] = int(list_jpg[k][7:13]) # time stamp from frame name
timestamp = timestamp/1000

from count_number_spots import spot_count

number_write = open("number.txt","w")

for k in range(len(list_jpg)-1):
    img_previous = path.join(folder_name+'/'+list_jpg[k])
    img_after = path.join(folder_name+'/'+list_jpg[k+1])
    keypoints_count = spot_count(img_previous, img_after)
    number_write.write(str(keypoints_count)+"\n")
    if k>4680:
        break
    
number_write.close()
    
    
    