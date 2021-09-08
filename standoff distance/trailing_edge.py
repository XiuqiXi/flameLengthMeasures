# -*- coding: utf-8 -*-
"""
Created on Tue Sep  7 11:40:30 2021

@author: xixiu
"""

import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt
from scipy.optimize import curve_fit

def func(x, a):
    return a*x**(1/2)

def stand_off(img):

    img = cv.imread(img)
    
    img_cropped = img[330:580, 180:, :]
    
    [b, g, r] = cv.split(img_cropped)
    img_theshold = b
    
    T, img_theshold = cv.threshold(img_theshold, 210, 255, cv.THRESH_BINARY)
    
    edges = cv.Canny(img_theshold,30,200)
    
    # cv.imshow("result", img_cropped)
    
    M = np.nonzero(edges)
    
    Y = M[0]
    X = M[1]
    popt, pcov = curve_fit(func, X, Y)
    perr=np.sqrt(np.diag(pcov))
    a = popt[0] 
    y_predict = func(X, a)
    SS_R = sum((Y-y_predict)**2)
    SS_T = sum((Y-np.mean(Y))**2)
    r_square = 1-(float(SS_R))/SS_T
    
    
    # M_list = M[1].tolist()
    
    # M_max = max(M_list)
    
    # M_max_index = M_list.index(M_max)
    
    
    # standoff = M[0][M_max_index]
    
    return a, r_square

A, B = stand_off("1.jpeg")

    
# img_cropped = img[558:658, 24:580, :]

# # img_cropped = img

# img_theshold = cv.cvtColor(img_cropped, cv.COLOR_BGR2GRAY)

# [b, g, r] = cv.split(img_cropped)
# img_theshold = b
# T, img_theshold = cv.threshold(img_theshold, 15, 255, cv.THRESH_BINARY)

# edges = cv.Canny(img_theshold,30,200)


# inte_col = []

# for i in range(0, img_theshold.shape[1]-1):
#     temp = sum(edges[:,i])/edges.shape[0]
#     inte_col.append(temp)

# sum_all_pixels = np.sum(img_theshold)

# flame_length = sum_all_pixels/255/img_theshold.shape[0]

# for k in range(int(flame_length*0.8), 0, -1):
#     if (sum(edges[:,k])/edges.shape[0] > 50):
#         #print(sum(img_theshold[:,k])/img_theshold.shape[0])
#         break
    
# # plt.imshow(img_theshold)
# # cv.imshow("result", edges)

# # print(int(flame_length*0.8))
# edges_loc = k*0.332103321