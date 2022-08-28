import cv2
import mediapipe as mp
import time
import pydirectinput as con
import pyautogui as gui
gui.PAUSE = 0.001

cap = cv2.VideoCapture(0)

mpHands = mp.solutions.hands
hands = mpHands.Hands()
mpDraw = mp.solutions.drawing_utils

pTime = 0
cTime = 0
ubx = 50
uby = 50

sw, sh = gui.size()
himg = 480
wimg = 640
uby = 0
while True:
    _, img = cap.read()
    img = cv2.flip(img, 1)
    frameRGB = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)
    results = hands.process(frameRGB)
    # print(results.multi_hand_landmarks)

    if results.multi_hand_landmarks:
        for handLms in results.multi_hand_landmarks:
            for id, lm in enumerate(handLms.landmark):
                cx, cy = int(lm.x * wimg), int(lm.y * himg)
                if id == 9:
                    ubx = int(sw/wimg*cx)
                    uby = int(sh/himg*cy)
                    gui.moveTo(ubx, uby)
                    cv2.circle(img, (cx, cy), 15, (255, 0, 255), cv2.FILLED)
                if id == 12:
                    cx, cy = int(lm.x * wimg), int(lm.y * himg)
                    ubyti = int(sh/himg*cy)
                    if abs(ubyti - uby) < 60:
                        con.rightClick()
                        time.sleep(0.03)
                if id == 5:
                    cx, cy = int(lm.x * wimg), int(lm.y * himg)
                    ubyfi = int(sh/himg*cy)
                if id == 8:
                    cx, cy = int(lm.x * wimg), int(lm.y * himg)
                    ubytifi = int(sh/himg*cy)
                    if abs(ubytifi - ubyfi) < 60:
                        con.click()
                        time.sleep(0.03)
            mpDraw.draw_landmarks(img, handLms, mpHands.HAND_CONNECTIONS)

    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime

    cv2.putText(img, str(int(fps)), (10, 70), cv2.FONT_HERSHEY_PLAIN, 3,
                (255, 0, 255), 3)