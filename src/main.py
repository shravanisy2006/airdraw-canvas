import cv2
import mediapipe as mp 

mp_hands = mp.solutions.hands
mp_draw = mp.solutions.drawing_utils

hands = mp_hands.Hands()

#Open camera
cam = cv2.VideoCapture(0)

while True:

    ret, frame = cam.read()

    rgb_frame = cv2.cvtColor(frame , cv2.COLOR_BGR2RGB)

    results = hands.process(rgb_frame)

    if results.multi_hand_landmarks:

        for hand_landmarks in results.multi_hand_landmarks:
            mp_draw.draw_landmarks(
                frame,
                hand_landmarks,
                mp_hands.HAND_CONNECTIONS
            )

            cv2.line(frame,(100,100),(300,100),(255,0,0),30)
            cv2.rectangle(frame,(100,100),(300,200),(0,255,255),10)
            cv2.circle(frame,(150,150),50,(0,0,255),3)

            cv2.putText(frame,"Air Canvas- Day 2",(50,50),cv2.FONT_HERSHEY_COMPLEX,1.5,(0,0,255),4)

    cv2.imshow("webcam",frame)
    if cv2.waitKey(1) == 27:
        break

cam.release()
cv2.destroyAllWindows()

