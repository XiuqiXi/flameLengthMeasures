# -*- coding: utf-8 -*-
"""
Created on Fri Sep 18 09:34:46 2020

@author: xixiu
"""
import numpy as np
from scipy.stats import kstest

def delete_data(data):
    for k in range(0,len(data)-10):
        if data[k]>100:
            data[k] = (data[k-20]+data[k+10])/2
            
    for k in range(0,len(data)-10):
        if data[k]<2:
            data[k] = (data[k-20]+data[k+10])/2
            
    window= np.ones(int(30))/float(30)
    average_data = np.convolve(data, window, 'same') 
    
    for n in range(2):
        for k in range(0,len(data)-10):
            if abs(data[k]-average_data[k])>1.5*abs(data[k-5]-average_data[k-5]):
                data[k] = (data[k-5]+data[k+5])/2
                
    return data

def get_deviation(data):
    data_upper = np.zeros(len(data))
    data_lower = np.zeros(len(data))
    data_mean = np.zeros(len(data))
    
    n = 5
    for k in range(n, len(data)-n):
        data_upper[k] = data[k]+np.var(data[k-n:k+n])
        data_lower[k] = data[k]-np.var(data[k-n:k+n])
        data_mean[k] = np.mean(data[k-n:k+n])
        
    return data_upper, data_lower, data_mean

def test_normality(data):
    p = np.zeros(len(data))
    
    n = 100
    for k in range(n, len(data)-n):
        test_results = kstest(data[k-n:k+n], 'norm')
        p[k] = test_results[1]
        
    return test_results