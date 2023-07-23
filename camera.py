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
    

    # Camera

def save_image(output_folder, image):
    # Generate a filename with a unique name
    filename = f"captured_image_{len(os.listdir(output_folder))}.jpg"
    output_path = os.path.join(output_folder, filename)
    cv2.imwrite(output_path, image)
    print(f"Image saved to: {output_path}")
    return True

def capture():
    # Output folder for saving the captured images
    output_folder = "temp_img"

    # Create the output folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Open the camera
    camera = cv2.VideoCapture(0)

    # Flag to indicate if an image has been saved
    image_saved = False  

    while True:
        # Capture a frame from the camera
        ret, frame = camera.read()

        if not ret:
            print("Failed to capture frame.")
            break

        # Get the dimensions of the frame
        height, width = frame.shape[:2]

        # Calculate the size of the square
        size = min(height, width)

        # Extract the square region from the center of the frame
        top = (height - size) // 2
        left = (width - size) // 2
        frame = frame[top:top + size, left:left + size]

        # Display the square frame in a window
        cv2.imshow("Camera", frame)

        # Wait for a key press
        key = cv2.waitKey(1)

        # Press the spacebar to save the current frame as an image
        if key == ord(' ') and not image_saved:
            image_saved = save_image(output_folder, frame)

        # Press escape to quit
        if image_saved or key == 27:
            break

    # Release the camera and close the window
    camera.release()
    cv2.destroyAllWindows()





