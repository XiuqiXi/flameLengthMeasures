# -*- coding: utf-8 -*-
"""
Created on Wed Aug  5 21:06:13 2020

@author: xixiu
"""
import cv2 as cv
import numpy as np
def template_demo(image_previous, image_after):
    cv.namedWindow('template image', cv.WINDOW_NORMAL)
    cv.imshow("template image", image_previous)
    cv.namedWindow('target image', cv.WINDOW_NORMAL)
    cv.imshow("target image", image_after)
    methods = [cv.TM_SQDIFF_NORMED, cv.TM_CCORR_NORMED, cv.TM_CCOEFF_NORMED]   #3种模板匹配方法
    th, tw = image_previous.shape[:2]
    for md in methods:
        print(md)
        result = cv.matchTemplate(image_after, image_previous, md)
        min_val, max_val, min_loc, max_loc = cv.minMaxLoc(result)
        if md == cv.TM_SQDIFF_NORMED:
            tl = min_loc
        else:
            tl = max_loc
        br = (tl[0]+tw, tl[1]+th)   #br是矩形右下角的点的坐标
        cv.rectangle(image_after, tl, br, (0, 0, 255), 2)
        cv.namedWindow("match-" + np.str(md), cv.WINDOW_NORMAL)
        cv.imshow("match-" + np.str(md), image_after)