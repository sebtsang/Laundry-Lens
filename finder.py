import cv2
import os
import numpy as np
import matplotlib.pyplot as plt

def write_contours_to_file(filename,img_path,dic):
    img = cv2.imread(img_path)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    mask = cv2.inRange(gray, 130, 255   ,cv2.THRESH_BINARY)
    
    
    
    contours,_ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
    cont_img = cv2.drawContours(mask, contours, -1, (0, 255, 0), 1)
    cv2.imwrite("symbols/"+filename,cont_img)
    remove_bg("symbols/"+filename)

def remove_bg(file_path):
    img = cv2.imread(file_path, 1)

    tmp = cv2.cvtColor(img,cv2.COLOR_BGRA2GRAY)
    _, alpha = cv2.threshold(tmp, 0, 255, cv2.THRESH_BINARY_INV)
    b, g, r = cv2.split(img)
    rgba = [b, g, r, alpha]
    dst = cv2.merge(rgba, 4)
    cv2.imwrite(file_path, dst)

    
def locate_img_on_img(img_path,template_path, dic):

    img1 = cv2.imread(img_path, 0)
    img2 = cv2.imread(template_path, 0)

    sift = cv2.SIFT_create()

    kp1, des1 = sift.detectAndCompute(img1, None)
    kp2, des2 = sift.detectAndCompute(img2, None)

    FLANN_INDEX_KDTREE = 0
    index_params = dict(algorithm=FLANN_INDEX_KDTREE, trees=5)
    search_params = dict(checks=50)

    flann = cv2.FlannBasedMatcher(index_params, search_params)

    matches = flann.knnMatch(des1, des2, k=2)

    good_matches = []
    for m, n in matches:
        #Change integer to increase strictness
        if m.distance < 0.65 * n.distance:
            good_matches.append(m)

    img3 = cv2.drawMatches(img1, kp1, img2, kp2, good_matches[:10], None, flags=2)

    cv2.imshow('Matches', img3)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
















        # img1 = cv2.imread(img_path)  
    # img2 = cv2.imread(template_path) 

    # #sift
    # sift = cv2.SIFT_create()



    # keypoints_1, descriptors_1 = sift.detectAndCompute(img1,None)
    # keypoints_2, descriptors_2 = sift.detectAndCompute(img2,None)

    # #feature matching
    # bf = cv2.BFMatcher(cv2.NORM_L1, crossCheck=True)

    # matches = bf.match(descriptors_1,descriptors_2)
    # matches = sorted(matches, key = lambda x:x.distance)

    # img3 = cv2.drawMatches(img1, keypoints_1, img2, keypoints_2, matches[:50], img2, flags=2)
    # plt.imshow(img3),plt.show()