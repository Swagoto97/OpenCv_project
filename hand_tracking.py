import cv2 as cv
import mediapipe as mp
import time

mphands = mp.solutions.hands
hands = mphands.Hands()
mpdraw = mp.solutions.drawing_utils

cap = cv.VideoCapture(0)
while True:
    success, img = cap.read()
    imgRGB = cv.cvtColor(img, cv.COLOR_BGR2RGB)
    result = hands.process(imgRGB)

    if result.multi_hand_landmarks:
        for handlms in result.multi_hand_landmarks:
            for id, lm in enumerate(handlms.landmark):
                # print(id,lm)
                h, w, c = img.shape
                cx, cy = int(lm.x*w), int(lm.y * h)
                print(id, cx, cy)
            mpdraw.draw_landmarks(img, handlms, mphands.HAND_CONNECTIONS)

    cv.imshow("video", img)
    cv.waitKey(1)
