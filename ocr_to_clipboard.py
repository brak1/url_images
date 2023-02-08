#!/usr/bin/env python

import cv2
import pytesseract
import datetime
import clipboard

while True:
    # (1) Wait for user to trigger an image capture
    input("\nPress Enter to capture image...")

    # (2) Capture image from USB camera
    camera = cv2.VideoCapture(0)
    return_value, image = camera.read()
    camera.release()

    # (3) Save image to images subfolder with time-date stamp on file name
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    file_name = "images/captured_image_" + timestamp + ".png"
    print("File name:  " + file_name)
    cv2.imwrite(file_name, image)

    # (4) Process image with Pytesseract for OCR string
    pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
    text = pytesseract.image_to_string(image)

    # (5) Send string to clipboard
    clipboard.copy(text)
    print(text)
    print("OCR text copied to clipboard.")

    cv2.imshow('image',image)
    cv2.waitKey(0)
