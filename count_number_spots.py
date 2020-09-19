# -*- coding: utf-8 -*-
"""
Created on Wed Aug  5 15:57:18 2020

@author: xixiuqi
"""

import cv2 as cv

def spot_count(img_previous, img_after):
    '''
    The function gets the number of counted keynumbers.

    Parameters
    ----------
    img_previous : srting
        The previous one of the images coupled to obtain the spots.  
    img_after : string
        The latter one of the images coupled to obtain the spots.  

    Returns
    -------
    keypoints_count : int
        The detected number of the spots 

    '''
    # read the images
    img_previous = cv.imread(img_previous)
    img_after = cv.imread(img_after)
    
    # choose the blue channel
    [b, g, r] = cv.split(img_previous)
    img_previous_blue = b
    
    [b, g, r] = cv.split(img_after)
    img_after_blue = b
    
    # binarization of images
    # gray_img_previous = cv.cvtColor(img_previous, cv.COLOR_BGR2GRAY)
    # gray_img_after = cv.cvtColor(img_after, cv.COLOR_BGR2GRAY)
    
    # get the substracted images
    # img_substracted = cv.subtract(img_after_blue, img_previous_blue)
    
    # detect the edges of images
    #edges = cv.Canny(img_substracted,30,200)
    
    
    # cv.imshow("img_substracted_old", img_substracted)
    # cv.imshow("result", edges)
    
    #cv.imshow("img_previous", img_previous_blue)
    #cv.imshow("img_after", img_after_blue)
    
    # filter the images with adaptive threshold
    # th = cv.adaptiveThreshold(gray_img,255,cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY,11,2)
    # filter the image with fixed threhold
    # (T, img_substracted) = cv.threshold(img_substracted, 155, 255, cv.THRESH_BINARY)
    
    # cv.imshow("img", img)
    # cv.imshow("result", edges)
    

    # import the translation function
    from align_translation import aglin_translation_images
    
    # get the translation matrix
    warp_matrix = aglin_translation_images(img_previous_blue, img_after_blue)
    # translate the image
    img_after_blue = cv.warpAffine(img_after_blue, warp_matrix, (img_after_blue.shape[1],\
                                                          img_after_blue.shape[0]))
        
    # cv.imshow("img_previous", img_previous_blue)
    # cv.imshow("img_after", img_previous_blue)
    
    # get the substracted image
    img_substracted = cv.subtract(img_after_blue, img_previous_blue)

    #cv.imshow("img_substracted", img_substracted)

    # import the spot detect function
    from detect_feather import detect_spot_SBD
    
    # get the spots number
    keypoints_count = detect_spot_SBD(img_substracted)
    
    #cv.imshow("img_substracted_spotted", im_with_keypoints)
    
    return keypoints_count
