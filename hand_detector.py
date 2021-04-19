import cv2 as cv
import mediapipe as mp
import time


class handDectator():
    def __init__(self, mode=False, maxhand=2, dectation=0.5, tracking=0.5):
        self.mode = mode
        self.maxhand = maxhand
        self.dectation = dectation
        self.tracking = tracking
        self.mphands = mp.solutions.hands
        self.hands = self.mphands.Hands(self.mode, self.maxhand, self.dectation,
                                        self.tracking)
        self.mpdraw = mp.solutions.drawing_utils

    def findhands(self, img, draw=True):
        imgRGB = cv.cvtColor(img, cv.COLOR_BGR2RGB)
        self.result = self.hands.process(imgRGB)

        if self.result.multi_hand_landmarks:
            for handlms in self.result.multi_hand_landmarks:

                if draw:
                    self.mpdraw.draw_landmarks(
                        img, handlms, self.mphands.HAND_CONNECTIONS)
        return img

    def getposition(self, img, hand=0):
        lmlist = []
        if self.result.multi_hand_landmarks:
            handlms = self.result.multi_hand_landmarks[hand]

            for id, lm in enumerate(handlms.landmark):
                # print(id,lm)
                h, w, c = img.shape
                cx, cy = int(lm.x*w), int(lm.y * h)
                # print(id, cx, cy)
                lmlist.append([id, cx, cy])

        return lmlist


def main():
    cap = cv.VideoCapture(0)
    de = handDectator()
    while True:
        success, img = cap.read()
        img = de.findhands(img)
        lmlist = de.getposition(img)
        if len(lmlist) != 0:
            print(lmlist)

        cv.imshow("video", img)
        cv.waitKey(1)


if __name__ == "__main__":
    main()
