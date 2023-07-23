import cv2
import numpy as np
import os
import matplotlib.pyplot as plt
import camera.py

from camera import crop
from camera import capture
from finder import write_contours_to_file, locate_img_on_img

capture()

img = cv2.imread("temp_img/test_2.png")
crop_img_path = crop(img)


folder_path = 'image_db'
symbol_dict = {}

for filename in os.listdir(folder_path):
    if filename.endswith('.png'):
        image_path = os.path.join(folder_path, filename)
        write_contours_to_file(filename,image_path,symbol_dict)

# locate_img_on_img(crop_img_path,"temp_img/test_3.png",symbol_dict)
# locate_img_on_img(crop_img_path,"temp_img/t.png",symbol_dict)
locate_img_on_img(crop_img_path,"symbols/low_temp.png",symbol_dict)
locate_img_on_img(crop_img_path,"symbols/do_not_tumble_dry.png",symbol_dict)
locate_img_on_img(crop_img_path,"symbols/any_solvent_except_tetra.png",symbol_dict)
locate_img_on_img(crop_img_path,"symbols/do_not_bleach.png",symbol_dict)
locate_img_on_img(crop_img_path,"symbols/water_temp_40.png",symbol_dict)
locate_img_on_img(crop_img_path,"symbols/perm_press.png",symbol_dict)



# print(symbol_dict.keys())
# print(symbol_dict['tumble_dry'])
# cv2.imshow("A",symbol_dict['tumble_dry'])
# cv2.waitKey(0)
