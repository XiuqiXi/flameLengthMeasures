# -*- coding: utf-8 -*-
"""
Created on Tue Sep  1 10:04:53 2020

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

def flame_length_measure(img, threshold):
    img = cv.imread(img)
    
    img = img[143:1033, 24:561, :]
    
    # img_cropped = img[408:808, :, :]
    
    img_cropped = img
    
    
    [b, g, r] = cv.split(img_cropped)
    # img_theshold = b/255.0
    # # img_theshold = cv.cvtColor(img_cropped, cv.COLOR_BGR2GRAY)
    # # img_theshold = img_theshold/255
    # gamma = 1
    # img_theshold=np.power(img_theshold,gamma)
    img_theshold = b
    T, img_theshold = cv.threshold(img_theshold,threshold, 1, cv.THRESH_BINARY)
    
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
    
    
    # f, ax = plt.subplots(1,3)
    # ax[0].imshow(img)
    # ax[0].set_title('raw image',fontsize=24,color='k')
    # ax[1].imshow(b)
    # ax[1].set_title('blue channel',fontsize=24,color='k')
    # ax[2].imshow(img_theshold)
    # ax[2].set_title('threshold as 20',fontsize=24,color='k')
    
    # time.sleep(2)
    
  
    ptStart = (int(k) ,0)
    ptEnd = (int(k) ,890)
    point_color = (0, 0, 255)
    thickness = 8
    lineType = 4 
    cv.line(img, ptStart, ptEnd, point_color, thickness, lineType)

    # cv.imshow('sss', img)
    
    # flame_length = []
    # flame_length.append(leftmost[0])
    
    k = k*0.332103321
    
   
    return img
    #1589279017853
    #1589278877211
    #1589278977177
    #1589278734340
k = flame_length_measure('1589278734340-S5C3.jpeg', 50)