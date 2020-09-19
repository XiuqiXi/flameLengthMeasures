# -*- coding: utf-8 -*-
"""
Created on Wed Aug  5 19:19:53 2020

@author: xixiuqi
"""

import cv2 as cv

'''
    The following part is from OpenCV API to detect the feathers as SimpleBlobDetector.
    It can be accessed from https://docs.opencv.org/2.4/modules/features2d/doc
    /common_interfaces_of_feature_detectors.html?highlight=blob
    The boundaries of each feathers are connected firstly and extracted. Then the edges are detected.  
'''
def detect_spot_SBD(img_substracted):
    '''
    

    Parameters
    ----------
    img_substracted : unit 8 picture
        The subctrated image for spots detections
    Returns
    -------
    len(keypoints)  : int
        The number of counted points

    '''
    
    params = cv.SimpleBlobDetector_Params()
    #Potential parameters
    #params.minThreshold= 10 #Minimum threshold for brightness
    #params.maxThreshold = 255 #Maximum threshold for brightness
    params.thresholdStep = 5 #The threshld steps for brighness The smaller, more spots will be detected
    
    params.filterByColor = True #Color control
    #params.blobColor = 0 #detect the black spot only
    params.blobColor = 255 #detect the white color only
    
    params.filterByArea = True #control the area the pixels
    params.minArea = 2
    #params.maxArea=2000
    
    #params.filterByCircularity = True #control the roundness，
                            # roundness=(4π×area)/circumference^2
    #params.minCircularity = 0.3
    
    #params.filterByConvexity =True #control the convexity
                            #，convexity = area of spot/the area of convex hull
    #params.minConvexity = 1.0
    
    #params.filterByInertia = True# control ineria
    #params.minInertiaRatio = 0.2#More close to 1, more round
    
    # create the detection
    detector = cv.SimpleBlobDetector_create(params)
    # detect the substracted image
    keypoints = detector.detect(img_substracted) 
    #print("detect %ds pots" %len(keypoints))
    
    # draw the spots on the substracted image
    # im_with_keypoints=cv.drawKeypoints(img_substracted, keypoints, np.array([]), (0, 0, 0),
    #                                     cv.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
    #print("the circle center coor is ：")
    #for (x,y) in keypoints[0].convert(keypoints):
        #print(x,",", y)
        #cv.circle(im_with_keypoints, (x,y), 1, (255,0,255), 30)
    
    
    #cv.imshow("img_substracted_spotted", im_with_keypoints)
    
    return len(keypoints)