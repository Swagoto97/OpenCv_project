from ctypes import cast, POINTER
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
from comtypes import CLSCTX_ALL
import cv2
import numpy as np
import hand_detector as hd
import math
import screen_brightness_control as sbc


####################################################################
# Volumn control
####################################################################
# devices = AudioUtilities.GetSpeakers()
# interface = devices.Activate(
#     IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
# volume = cast(interface, POINTER(IAudioEndpointVolume))
# # volume.GetMute()
# # volume.GetMasterVolumeLevel()
# volrange = volume.GetVolumeRange()

# minvol = volrange[0]
# maxvol = volrange[1]
#########################################################################

camW, camH = 640, 480
dec = hd.handDectator(dectation=0.8)
cap = cv2.VideoCapture(0)
cap.set(3, camW)
cap.set(4, camH)
volbar = 400
volpar = 0
while True:
    success, img = cap.read()
    img = dec.findhands(img)
    lmlist = dec.getposition(img)
    if len(lmlist) != 0:

        x1, y1 = lmlist[4][1], lmlist[4][2]
        x2, y2 = lmlist[8][1], lmlist[8][2]
        cx, cy = (x1+x2)//2, (y1+y2)//2
        cv2.circle(img, (x1, y1), 8, (255, 10, 25), cv2.FILLED)
        cv2.circle(img, (x2, y2), 8, (255, 10, 25), cv2.FILLED)
        cv2.line(img, (x1, y1), (x2, y2), (255, 0, 255), 2)
        cv2.circle(img, (cx, cy), 5, (255, 0, 255), cv2.FILLED)

        leng = math.hypot(x2-x1, y2 - y1)
        # vol = np.interp(leng, [20, 185], [minvol, maxvol])
        volbar = np.interp(leng, [20, 185], [400, 150])
        volpar = np.interp(leng, [20, 185], [0, 100])
        sbc.set_brightness(int(volpar))
        # volume.SetMasterVolumeLevel(vol, None)
        # print(vol)
        # print(leng)
        if leng < 20:
            cv2.circle(img, (cx, cy), 5, (0, 255, 0), cv2.FILLED)
    cv2.rectangle(img, (70, 150), (85, 400), (0, 0, 255), 2)
    cv2.rectangle(img, (70, int(volbar)), (85, 400), (0, 0, 255), cv2.FILLED)
    cv2.putText(img, f"{int(volpar)}%", (60, 50),
                cv2.FONT_HERSHEY_SCRIPT_SIMPLEX, 1, (0, 0, 255), 3)

    # print(lmlist)
    cv2.imshow("video", img)
    cv2.waitKey(1)
