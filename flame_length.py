# -*- coding: utf-8 -*-
"""
Created on Mon Aug 10 09:14:38 2020

@author: xixiu
"""

import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

# # subfolder name
# folder_name = './S5C3_JPEG'
# # first frame name
# first_name = '1589278821971-S5C3.jpeg'

# file_name = folder_name + first_name

def flame_length_measure(img):
    img = cv.imread(img)
    
    img_cropped = img[143:1033, 24:561, :]
    # img_cropped = img[:, 24:561, :]
    
    # img_cropped = img
    
    [b, g, r] = cv.split(img_cropped)
    img_theshold = b
    
    # [b, g, r] = cv.split(img_cropped)
    # img_previous_blue = b
    # T, img_theshold = cv.threshold(img_cropped, 10, 255, cv.THRESH_BINARY)
    
    # edges = cv.Canny(img_theshold,30,200)
    
    inte_col = []
    
    for i in range(0, img_theshold.shape[1]-1):
        temp = sum(img_theshold[:,i])/img_theshold.shape[0]
        inte_col.append(temp)
    
    for k in range(img_theshold.shape[1]-1, 0, -1):
        if (sum(img_theshold[:,k])/img_theshold.shape[0] > 45):
            #print(sum(img_theshold[:,k])/img_theshold.shape[0])
            break
    # contours, hierarchy = cv.findContours(edges, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
    
    # cnt = contours[0]
    # #img_coutours = cv.drawContours(img_gray, [cnt], 0, (0, 255, 0), 3)
    
    # leftmost = tuple(cnt[cnt[:, :, 0].argmin()][0])
    # return_value = leftmost[0]
    # rightmost = tuple(cnt[cnt[:, :, 0].argmax()][0])
    
    # img2 = img_cropped.copy()
    # cv.circle(img2, leftmost, 5, (0, 255, 255), -1)
    # cv.circle(img2, rightmost, 5, (0, 255, 255), -1)
    
    f, ax = plt.subplots(1,2)
    ax[0].imshow(img)
    ax[0].set_title('raw image',fontsize=24,color='k')
    ax[1].imshow(b)
    ax[1].set_title('blue channel',fontsize=24,color='k')
    
    # flame_length = []
    # flame_length.append(leftmost[0])
    
    k = k*0.332103321
    
    return k
    
k = flame_length_measure('1589278798600-S5C3.jpeg')