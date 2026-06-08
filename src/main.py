import cv2
import mediapipe as mp 

mp_hands = mp.solutions.hands
mp_draw = mp.solutions.drawing_utils

hands = mp_hands.Hands(
    max_num_hands=1,
    min_detection_confidence=0.7,
    min_tracking_confidence=0.7
)

#Open camera
cam = cv2.VideoCapture(0)

cam.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

prev_x = None
prev_y = None

canvas = None

current_colour = (0,255,0)

key = 0

eraser = False

while True:

    ret, frame = cam.read()

    if canvas is None:
        canvas = frame.copy() * 0

    height , width , channels = frame.shape

    rgb_frame = cv2.cvtColor(frame , cv2.COLOR_BGR2RGB)

    results = hands.process(rgb_frame)

    if results.multi_hand_landmarks:

        for hand_landmarks in results.multi_hand_landmarks:
            index_finger = hand_landmarks.landmark[8]

            index_finger_tip = hand_landmarks.landmark[8]
            index_finger_joint = hand_landmarks.landmark[6]
            
            index_up = index_finger_tip.y < index_finger_joint.y

            middle_finger_tip = hand_landmarks.landmark[12]
            middle_finger_joint = hand_landmarks.landmark[10]

            middle_up = middle_finger_tip.y < middle_finger_joint.y

            x = int(index_finger.x *width)
            y = int(index_finger.y * height)

            #SELECTION MODE

            if index_up and middle_up:

                prev_x = None
                prev_y = None

                cv2.putText(frame,"Selection Mode",(10,80),cv2.FONT_HERSHEY_COMPLEX_SMALL,0.7,current_colour,2)

                if y < 30:

                    if x < 50:
                        current_colour = (0,0,255)
                        eraser = False

                    elif x < 100:
                        current_colour = (0,255,0)
                        eraser = False

                    elif x < 150:
                        current_colour = (255,0,0)
                        eraser = False

                    elif x < 200:
                        current_colour = (0,0,0)   # Eraser
                        eraser = True

                    elif x < 250:
                        canvas = frame.copy() * 0  # Clear
            
            #DRAWING MODE

            elif index_up:

                cv2.putText(frame,"Drawing Mode",(10,80),cv2.FONT_HERSHEY_COMPLEX_SMALL,0.7,current_colour,2)

                if prev_x is not None and prev_y is not None:

                    smooth_x = int((prev_x + x) / 2)
                    smooth_y = int((prev_y + y) / 2)

                    if eraser:
                        cv2.line(canvas, (prev_x, prev_y),
                                (smooth_x, smooth_y),
                                (0,0,0), 20)
                    else:
                        cv2.line(canvas, (prev_x, prev_y),
                                (smooth_x, smooth_y),
                                current_colour, 3)

                    prev_x = smooth_x
                    prev_y = smooth_y

                else:
                    prev_x = x
                    prev_y = y

            cv2.circle(frame, (x, y), 8, current_colour , -1)                

            mp_draw.draw_landmarks(
                frame,
                hand_landmarks,
                mp_hands.HAND_CONNECTIONS
            )

    frame = cv2.add(frame , canvas)

    cv2.rectangle(frame,(0,0),(50,30),(0,0,255),-1)
    cv2.rectangle(frame,(50,0),(100,30),(0,255,0),-1)
    cv2.rectangle(frame,(100,0),(150,30),(255,0,0),-1)
    cv2.rectangle(frame, (150,0),(200,30),(255,255,255),-1)
    cv2.rectangle(frame,(200,0),(250,30),(0,0,0),-1)

    cv2.putText(frame,"R",(15,20),cv2.FONT_HERSHEY_SIMPLEX,0.5,(255,255,255),1)
    cv2.putText(frame,"G",(65,20),cv2.FONT_HERSHEY_SIMPLEX,0.5,(0,0,0),1)
    cv2.putText(frame,"B",(115,20),cv2.FONT_HERSHEY_SIMPLEX,0.5,(255,255,255),1)
    cv2.putText(frame,"E",(165,20),cv2.FONT_HERSHEY_SIMPLEX,0.5,(0,0,0),1)
    cv2.putText(frame,"C",(215,20),cv2.FONT_HERSHEY_SIMPLEX,0.5,(255,255,255),1)

    cv2.imshow("webcam",frame)

    key = cv2.waitKey(1) & 0xFF
    if key == ord('s'):
        cv2.imwrite("drawing.png",canvas)
        print("Drawing Saved")

    elif key == 27:
        break;

cam.release()
cv2.destroyAllWindows()