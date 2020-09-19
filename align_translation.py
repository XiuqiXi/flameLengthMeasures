# -*- coding: utf-8 -*-
"""
Created on Wed Aug  5 21:35:00 2020

@author: xixiuqi
"""

import numpy as np
import cv2

def aglin_translation_images(im1, im2):
    '''
    

    Parameters
    ----------
    im1 : unit 8 picture
        The image is translated.
    im2 : unit 8 picture
        The target image

    Returns
    -------
    warp_matrix : array
        translation matrix

    '''
    # convert the images to gray images
    im1_gray = im1
    im2_gray = im2
    # define the transformation is only translation
    warp_mode = cv2.MOTION_TRANSLATION
    # create the 2*3 translation matrix 
    warp_matrix = np.eye(2, 3, dtype=np.float32)
    # set the number o iternations
    number_of_iterations = 5000;
    # set the termination conditions
    termination_eps = 1e-10;
    # get the ECC criteria
    criteria = (cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_COUNT, number_of_iterations,  termination_eps)
    # run ECC and get the translation matrix
    (cc, warp_matrix) = cv2.findTransformECC (im1_gray,im2_gray,warp_matrix, warp_mode, criteria)
    
    return warp_matrix