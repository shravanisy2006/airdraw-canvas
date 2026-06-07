import cv2
import mediapipe as mp 

mp_hands = mp.solutions.hands
mp_draw = mp.solutions.drawing_utils

hands = mp_hands.Hands()

#Open camera
cam = cv2.VideoCapture(0)

while True:

    ret, frame = cam.read()

    height , width , channels = frame.shape

    rgb_frame = cv2.cvtColor(frame , cv2.COLOR_BGR2RGB)

    results = hands.process(rgb_frame)

    if results.multi_hand_landmarks:

        for hand_landmarks in results.multi_hand_landmarks:
            index_finger = hand_landmarks.landmark[8]

            x = int(index_finger.x *width)
            y = int(index_finger.y * height)
            
            cv2.circle(frame, (x, y), 10, (0, 255, 0), -1)

            mp_draw.draw_landmarks(
                frame,
                hand_landmarks,
                mp_hands.HAND_CONNECTIONS
            )

            cv2.putText(frame,"Air Canvas",(50,50),cv2.FONT_HERSHEY_COMPLEX,1.5,(0,0,255),2)

    cv2.imshow("webcam",frame)
    if cv2.waitKey(1) == 27:
        break

cam.release()
cv2.destroyAllWindows()

