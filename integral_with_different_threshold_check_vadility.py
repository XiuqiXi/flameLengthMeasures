# -*- coding: utf-8 -*-
"""
Created on Fri Sep 18 10:49:08 2020

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
    
    # img = img[143:1033, 24:561, :]
    img_cropped = img[:, 24:561, :]
    
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
        if (sum(img_theshold[:,k])/img_theshold.shape[0] > 2):
            #print(sum(img_theshold[:,k])/img_theshold.shape[0])
            k_2 = k
            break
        
    for k in range(img_theshold.shape[1]-1, 0, -1):
        if (sum(img_theshold[:,k])/img_theshold.shape[0] > 15):
            #print(sum(img_theshold[:,k])/img_theshold.shape[0])
            k_15 = k
            break
    
    for k in range(img_theshold.shape[1]-1, 0, -1):
        if (sum(img_theshold[:,k])/img_theshold.shape[0] > 30):
            #print(sum(img_theshold[:,k])/img_theshold.shape[0])
            k_30 = k
            break
    
    for k in range(img_theshold.shape[1]-1, 0, -1):
        if (sum(img_theshold[:,k])/img_theshold.shape[0] > 45):
            #print(sum(img_theshold[:,k])/img_theshold.shape[0])
            k_45 = k
            break
        
    for k in range(img_theshold.shape[1]-1, 0, -1):
        if (sum(img_theshold[:,k])/img_theshold.shape[0] > 60):
            #print(sum(img_theshold[:,k])/img_theshold.shape[0])
            k_60 = k
            break
        
    for k in range(img_theshold.shape[1]-1, 0, -1):
        if (sum(img_theshold[:,k])/img_theshold.shape[0] > 75):
            #print(sum(img_theshold[:,k])/img_theshold.shape[0])
            k_75 = k
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
    
    f, ax = plt.subplots(2,4)
    ax[0,0].imshow(img)
    ax[0,0].set_title('raw image',fontsize=24,color='k')
    ax[0,1].imshow(b)
    ax[0,1].set_title('blue channel',fontsize=24,color='k')
    
    ax1 = ax[0,2]
    ax1.imshow(b, cmap = 'bone')
    ax2 = ax[0,2].twinx()
    ax2.plot(inte_col, color='r', linewidth=5)
    ax2.axhline(y=2, xmin=0.05, xmax=1, linestyle = "--", color='r')
    ax2.axvline(x=k_2, ymin=0, ymax=1, linestyle = "--", color='yellow', linewidth=3)
    ax[0,2].set_title('threshold 2',fontsize=24,color='k')
    
    ax1 = ax[0,3]
    ax1.imshow(b, cmap = 'bone')
    ax2 = ax[0,3].twinx()
    ax2.plot(inte_col, color='r', linewidth=5)
    ax2.axhline(y=15, xmin=0.05, xmax=1, linestyle = "--", color='r')
    ax2.axvline(x=k_15, ymin=0, ymax=1, linestyle = "--", color='yellow', linewidth=3)
    ax[0,3].set_title('threshold 15',fontsize=24,color='k')
    
    ax1 = ax[1,0]
    ax1.imshow(b, cmap = 'bone')
    ax2 = ax[1,0].twinx()
    ax2.plot(inte_col, color='r', linewidth=5)
    ax2.axhline(y=30, xmin=0.05, xmax=1, linestyle = "--", color='r')
    ax2.axvline(x=k_30, ymin=0, ymax=1, linestyle = "--", color='yellow', linewidth=3)
    ax[1,0].set_title('threshold 30',fontsize=24,color='k')
    
    ax1 = ax[1,1]
    ax1.imshow(b, cmap = 'bone')
    ax2 = ax[1,1].twinx()
    ax2.plot(inte_col, color='r', linewidth=5)
    ax2.axhline(y=45, xmin=0.05, xmax=1, linestyle = "--", color='r')
    ax2.axvline(x=k_45, ymin=0, ymax=1, linestyle = "--", color='yellow', linewidth=3)
    ax[1,1].set_title('threshold 45',fontsize=24,color='k')
    
    ax1 = ax[1,2]
    ax1.imshow(b, cmap = 'bone')
    ax2 = ax[1,2].twinx()
    ax2.plot(inte_col, color='r', linewidth=5)
    ax2.axhline(y=60, xmin=0.05, xmax=1, linestyle = "--", color='r')
    ax2.axvline(x=k_60, ymin=0, ymax=1, linestyle = "--", color='yellow', linewidth=3)
    ax[1,2].set_title('threshold 60',fontsize=24,color='k')
    
    ax1 = ax[1,3]
    ax1.imshow(b, cmap = 'bone')
    ax2 = ax[1,3].twinx()
    ax2.plot(inte_col, color='r', linewidth=5)
    ax2.axhline(y=75, xmin=0.05, xmax=1, linestyle = "--", color='r')
    ax2.axvline(x=k_75, ymin=0, ymax=1, linestyle = "--", color='yellow', linewidth=3)
    ax[1,3].set_title('threshold 75',fontsize=24,color='k')
    
    
    
    # ax[2].set_ylim(0,100)
    # ax[2].set_title('threshold as 20',fontsize=24,color='k')
    
    # flame_length = []
    # flame_length.append(leftmost[0])
    
    k = k*0.332103321
    
    return k
    
k = flame_length_measure('1589278643396-S5C3.jpeg')