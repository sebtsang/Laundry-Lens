import cv2
import os
import numpy as np
import matplotlib.pyplot as plt
from roboflow import Roboflow
rf = Roboflow(api_key="I1mlRB3M8fNGO0N3XG4W")
project = rf.workspace().project("care_symbols")
model = project.version(7).model



def match(img_path, dic):
    symbol_name = []
    count = 0
    prediction = (model.predict(img_path, confidence=40, overlap=30).json())
    model.predict(img_path, confidence=40, overlap=30).save("prediction.png")
    n = 0
    for n in prediction["predictions"]:
        symbol_name.append(n['class'])
        
        count+=1
    return symbol_name








