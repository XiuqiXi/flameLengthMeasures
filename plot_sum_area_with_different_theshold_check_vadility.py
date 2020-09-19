# -*- coding: utf-8 -*-
"""
Created on Fri Sep 18 09:23:12 2020

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
    
    img = img[:, 24:561, :]
    
    # img_cropped = img[408:808, :, :]
    
    img_cropped = img
    
    
    [b, g, r] = cv.split(img_cropped)
    # img_theshold = b/255.0
    # # img_theshold = cv.cvtColor(img_cropped, cv.COLOR_BGR2GRAY)
    # # img_theshold = img_theshold/255
    # gamma = 1
    # img_theshold=np.power(img_theshold,gamma)
    img_theshold = b
    T, img_theshold_2 = cv.threshold(b,2, 1, cv.THRESH_BINARY)
    T, img_theshold_15 = cv.threshold(b,15, 1, cv.THRESH_BINARY)
    T, img_theshold_30 = cv.threshold(b,30, 1, cv.THRESH_BINARY)
    T, img_theshold_45 = cv.threshold(b,45, 1, cv.THRESH_BINARY)
    T, img_theshold_60 = cv.threshold(b,60, 1, cv.THRESH_BINARY)
    T, img_theshold_75 = cv.threshold(b,75, 1, cv.THRESH_BINARY)
    
    # edges = cv.Canny(img_theshold,30,200)
    
    sum_all_pixels = np.sum(img_theshold)
    
    # sum_all_pixels = img_theshold.shape[0]*img_theshold.shape[1]*255-sum_all_pixels
    
    k = sum_all_pixels/img_theshold.shape[0]

    # contours, hierarchy = cv.findContours(edges, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
    
    # cnt = contours[0]
    # #img_coutours = cv.drawContours(img_gray, [cnt], 0, (0, 255, 0), 3)
    
    # leftmost = tuple(cnt[cnt[:, :, 0].argmin()][0])
    # return_value = leftmost[0]
    # rightmost = tuple(cnt[cnt[:, :, 0].argmax()][0])
    
    # img2 = img_cropped.copy()
    # cv.circle(img2, leftmost, 5, (0, 255, 255), -1)
    # cv.circle(img2, rightmost, 5, (0, 255, 255), -1)
    
    
    f, ax = plt.subplots(2,4)
    ax[0,0].imshow(img)
    ax[0,0].set_title('raw image',fontsize=20,color='k')
    ax[0,1].imshow(b)
    ax[0,1].set_title('blue channel',fontsize=20,color='k')
    ax[0,2].imshow(img_theshold_2)
    ax[0,2].set_title('threshold as 2',fontsize=20,color='k')
    ax[0,3].imshow(img_theshold_15)
    ax[0,3].set_title('threshold as 15',fontsize=20,color='k')
    ax[1,0].imshow(img_theshold_30)
    ax[1,0].set_title('threshold as 30',fontsize=20,color='k')
    ax[1,1].imshow(img_theshold_45)
    ax[1,1].set_title('threshold as 45',fontsize=20,color='k')
    ax[1,2].imshow(img_theshold_60)
    ax[1,2].set_title('threshold as 60',fontsize=20,color='k')
    ax[1,3].imshow(img_theshold_75)
    ax[1,3].set_title('threshold as 75',fontsize=20,color='k')
    # time.sleep(2)

    
    # flame_length = []
    # flame_length.append(leftmost[0])
    
    k = k*0.332103321
    
   
    return k
    #1589279017853
    #1589278877211
    #1589278977177
    #1589278734340
k = flame_length_measure('1589278643396-S5C3.jpeg')