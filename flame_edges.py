# -*- coding: utf-8 -*-
"""
Created on Sun Sep 13 21:38:58 2020

@author: xixiu
"""

import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

# # subfolder name
# folder_name = './S5C3_JPEG'
# # first frame name
# img = '1589278734373-S5C3.jpeg'

# file_name = folder_name + first_name

def flame_edges_measure(img):
    img = cv.imread(img)
    
    img_cropped = img[558:658, 24:580, :]
    
    # img_cropped = img
    
    img_theshold = cv.cvtColor(img_cropped, cv.COLOR_BGR2GRAY)
    
    [b, g, r] = cv.split(img_cropped)
    img_theshold = b
    T, img_theshold = cv.threshold(img_theshold, 15, 255, cv.THRESH_BINARY)
    
    edges = cv.Canny(img_theshold,30,200)
    
    
    inte_col = []
    
    for i in range(0, img_theshold.shape[1]-1):
        temp = sum(edges[:,i])/edges.shape[0]
        inte_col.append(temp)
    
    sum_all_pixels = np.sum(img_theshold)
    
    flame_length = sum_all_pixels/255/img_theshold.shape[0]
    
    for k in range(int(flame_length*0.8), 0, -1):
        if (sum(edges[:,k])/edges.shape[0] > 50):
            #print(sum(img_theshold[:,k])/img_theshold.shape[0])
            break
        
    # plt.imshow(img_theshold)
    # cv.imshow("result", edges)
    
    # print(int(flame_length*0.8))
    edges_loc = k*0.332103321

    return edges_loc

def flame_edges_measure_sum(img):
    img = cv.imread(img)
    
    # img_cropped = img[558:658, 24:580, :]
    
    img_cropped = img[:, 38:561, :]
    
    # img_cropped = img
    
    img_theshold = cv.cvtColor(img_cropped, cv.COLOR_BGR2GRAY)
    
    [b, g, r] = cv.split(img_cropped)
    img_theshold = b
    T, img_theshold = cv.threshold(b, 15, 255, cv.THRESH_BINARY_INV)
    
    T, img_theshold_f = cv.threshold(b, 15, 255, cv.THRESH_BINARY)   

    
    sum_all_pixels = np.sum(img_theshold_f)
    
    flame_length = sum_all_pixels/255/img_theshold.shape[0]
    
    img_theshold = img_theshold[:, 0:int(flame_length*0.3)]
    
    sum_all_pixels  = np.sum(img_theshold)
    
    k = sum_all_pixels/img_theshold.shape[0]/255

        
    # plt.imshow(img)
    # cv.imshow("result", img_theshold)
    
    # print(int(flame_length*0.8))
    edges_loc = k*0.332103321

    return edges_loc

k = flame_edges_measure('1589278769816-S5C3.jpeg')