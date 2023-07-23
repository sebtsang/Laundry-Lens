import cv2
import numpy as np
import os
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import ttk
from PIL import ImageTk, Image

from camera import crop
from finder import match






def next():
    root = tk.Tk()
    root.title("Laundry Lens")
    root.geometry("800x600")
    raw_img = cv2.imread("temp_img/raw.png")
    crop(raw_img)
    symbols = match("temp_img/raw.png",symbol_dict)
    photo = tk.PhotoImage(file= "prediction.png")
    panel = tk.Label(root, image=photo)
    panel.pack(side="top", fill='x')
    text_desc = 'Meanings:\n'
    
    label = tk.Label(root, text=text_desc)
    pac
    label.pack(side="bottom",pady=20)

    root.mainloop()

def video_stream():
    # Read a frame from the camera
    ret, frame = cap.read()
    if ret:
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        # Create an image from the frame
        img = Image.fromarray(frame)

        # Create an imageTk object from the image
        imgtk = ImageTk.PhotoImage(image=img)

        # Set the imageTk object as the image for the label
        label.imgtk = imgtk
        label.configure(image=imgtk)

    # Call this function again after 10 milliseconds
    label.after(10, video_stream)

def take_photo(event):
    _, frame = cap.read()
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    cv2.imwrite("temp_img/raw.png", frame)
    root.destroy()
    next()
    return False

#window
root = tk.Tk()
root.title("Laundry Lens")
root.geometry("800x600")

title_label = ttk.Label(master=root, text='Press Space to Take a Photo', font='Calibri 24 bold')
cap = cv2.VideoCapture(0)


label = ttk.Label(root)
label.pack()






symbol_dict = {"30C": "Wash at or below 30 degrees celsius", "40C" : "Wash at or below 40 degrees celsius" ,
            "50C" : "Wash at or below 50 degrees celsius", "60C" : "Wash at or below 60 degrees celsius", 
            "70C" : "Wash at or below 70 degrees celsius", "90C" : "Wash at or below 90 degrees celsius", 
            "95C" : "Wash at or below 95 degrees celsius", "DN_bleach" : "Do not bleach", 
            "DN_dry_clean" : "Do not dry clean", "DN_iron" : "Do not iron", "DN_steam" : "Do not steam", 
            "DN_tumble_dry" : "Do not tumble dry" , "DN_wash" : "Do not wash", "DN_wet_clean" : "Do not wet clean",
            "DN_wring" : "Do not wring", "bleach" : "bleach", "bleach_color" : "Non-chlorine bleach", 
            "chlorine_bleach" : "Chlorine bleach", "drip_dry" : "drip dry", "drip_dry_in_shade" : "drip dry in shade",
            "dry_clean" : "dry clean safe", "dry_clean_any_solvent" : "dry clean any solvent",
            "dry_clean_any_solvent_except_trichloroethylene" : "dry clean any solvent except trichloroethylene", 
            "dry_clean_any_solvent_except_trichloroethylene_delicate" : "dry clean any solvent except trichloroethylene and delicate",
            "dry_clean_any_solvent_except_trichloroethylene_very_delicate" : "dry clean any solvent except trichloroethylene and very delicate",
            "dry_clean_low_heat": "dry clean with low heat", "dry clean no steam" : "dry clean but no steam", 
            "dry_clean_petrol_only" : "dry clean petroleum only", "dry_clean_petrol_only_delicate": "dry clean with petrol only, delicate",
            "dry_clean_petrol_only_very_delicate" : "dry clean with petrol only, very delicate",
            "dry_clean_reduced_moisture" : "dry clean with reduced moisture", "dry_clean_short_cycle" : "dry clean short cycle",
            "dry_flat" : "dry flat", "dry_flat_in_shade" : "dry flat in shade", "hand_wash" : "hand wash", "iron" : "iron safe", "iron_high" : "iron at high temperature",
            "iron_low" : "iron at low temperature", "iron_medium" : "iron at medium temperature", "line_dry" : "line dry",
            "line_dry_in_shade" : "line dry in shade", "machine_wash_delicate" : "machine wash delicate", 
            "machine_wash_normal" : "machine wash delicate", "machine_wash_permanent_press" : "machine wash perm press",
            "natural_dry" : "natural dry", "non_chlorine_bleach" : "non-chlorine bleach", "shade_dry" : "shade dry", "steam" : "steam safe", "tumble_dry_delicate" : "tumble dry on delicate", 
            "tumble_dry_high" : "tumble dry on high temp", "tumble_dry_low" : "tumble dry on low temp", 
            "tumble_dry_medium" : "tumble dry on medium temp", "tumble_dry_no_heat" : "tumble dry no heat",
            "tumble_dry_normal" : "tumble dry normal", "tumble_dry_very_delicate" : "tumble dry very delicate",
            "wet_clean" : "wet clean", "wet_clean_delicate" : "wet clean, delicate", "wet_clean_very_delicate" : "wet clean, very delicate",
            "wring" : "wring safe"}

x = True
x = root.bind("<space>", take_photo)


video_stream()
root.mainloop()    













