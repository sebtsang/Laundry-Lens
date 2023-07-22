import cv2
import os
import numpy as np
import matplotlib.pyplot as plt

def crop(img):
    #light threshold 0-255
    lower = np.array([100,100,100])
    higher = np.array([245,245,245])
    
    mask = cv2.inRange(img,lower,higher)
    cont,_ = cv2.findContours(mask,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)

    #cont_img = cv2.drawContours(img,cont,-1,255,3)

    area = max(cont,key=cv2.contourArea)
    x,y,w,h = cv2.boundingRect(area)
    cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
    cropped_image = img[y:y+h,x:x+w]

    # cv2.imshow("Image",img)
    # cv2.waitKey(0)
    # cv2.imshow("Image",cropped_image)
    # cv2.waitKey(0)
    cv2.imwrite("temp_img/cropped.png",cropped_image)
    return "temp_img/cropped.png"
    





