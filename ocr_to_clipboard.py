#!/usr/bin/env python

import cv2
import pytesseract
import datetime
import clipboard

# (1) Wait for user to trigger an image capture
input("Press Enter to capture image...")

# (2) Capture image from USB camera
print("starting camera = cv2.VideoCapture(0)"); 
camera = cv2.VideoCapture(0)
print("starting image = camera.read()") 
return_value, image = camera.read()
print("starting camera.release()")
camera.release()

# (3) Save image to images subfolder with time-date stamp on file name
print("starting timestamp = datetime.datetime.now().strftime(...)")
timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
print(timestamp)
print("starting file_name = ""images/captured_image_"" + timestamp + "".png""")
file_name = "images/captured_image_" + timestamp + ".png"
print(file_name)
print("starting cv2.imwrite(file_name, image)")
cv2.imwrite(file_name, image)

# (4) Process image with Pytesseract for OCR string
print("starting text = pytesseract.image_to_string(image)")
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
text = pytesseract.image_to_string(image)

# (5) Send string to clipboard
clipboard.copy(text)
print(text)
print("OCR text copied to clipboard.")
