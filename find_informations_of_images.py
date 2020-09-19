# -*- coding: utf-8 -*-
"""
Created on Thu Aug 27 09:54:04 2020

@author: xixiu
"""

import cv2 as cv
import matplotlib.pyplot as plt

def get_pyrolysis_front(img):
    img = cv.imread(img)
    
    img = img[143:1033, 24:561, :]
    # img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    # (T, img) = cv.threshold(img, 10, 255, cv.THRESH_BINARY)
    
    a = []
    
    def on_EVENT_LBUTTONDOWN(event, x, y, flags, param):
        if event == cv.EVENT_LBUTTONDOWN:
            xy = "%d,%d" % (x, y)
            a.append(x)
            cv.circle(img, (x, y), 1, (0, 0, 255), thickness=-1)
            cv.putText(img, xy, (x, y), cv.FONT_HERSHEY_PLAIN,
                        1.0, (0, 0, 255), thickness=1)
            cv.imshow("image", img)
            cv.destroyAllWindows()
    
    cv.namedWindow("image")
    cv.setMouseCallback("image", on_EVENT_LBUTTONDOWN)
    cv.imshow("image", img)
    cv.waitKey(0)
    return a

a = get_pyrolysis_front('1589278701274-S5C3.jpeg')