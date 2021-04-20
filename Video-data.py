import cv2

import numpy as np
import pytesseract

pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'

cap = cv2.VideoCapture(0)
cap.set(3, 640)
cap.set(4, 480)

while True:
    s, img = cap.read()
    imgh, imgw, _ = img.shape
    boxes = pytesseract.image_to_data(img)
    for a, b in enumerate(boxes.splitlines()):
        # print(b)
        if a != 0:
            b = b.split()
            if len(b) == 12:
                x, y, w, h = int(b[6]), int(b[7]), int(b[8]), int(b[9])
                cv2.putText(img, b[11], (x, y-5),
                            cv2.FONT_HERSHEY_SIMPLEX, 1, (50, 50, 255), 2)
                cv2.rectangle(img, (x, y), (x+w, y+h), (50, 50, 255), 2)
                # print(b[11])
    cv2.imshow("Result", img)
    cv2.waitKey(1)