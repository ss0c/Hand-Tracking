#Importamos todas las librerias necesarias

import cv2
import mediapipe as mp
import time

cap = cv2.VideoCapture(0)
mp_hands = mp.solutions.hands
mp_draw = mp.solutions.drawing_utils
hands = mp_hands.Hands()


while True:

    frame, img = cap.read()
    imgRGB = cv2.cvtColor(img,cv2.COLOR_BGR2RGB) # CONVERTIMOS LA IMAGEN DE LA CAMARA EN RGB
    results = hands.process(imgRGB)
    #print(results.multi_hand_landmarks)

    if results.multi_hand_landmarks:
        for handLms in results.multi_hand_landmarks:
            #print(handLms)
            for id , lm in enumerate(handLms.landmark):
                print(lm)
                print(id)
                h, w, c = img.shape
                cx, cy = int(lm.x * w), int(lm.y * h)
                print(id, cx, cy)


                cv2.circle(img,(cx,cy), 15,(255,0,255), cv2.FILLED)

            mp_draw.draw_landmarks(img,handLms, mp_hands.HAND_CONNECTIONS)




    cv2.imshow("Video",img)
    cv2.waitKey(1)
