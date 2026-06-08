1. import cv2 imports the OpenCV library into Python.

2. VideoCapture(0) opens the default webcam.
   - 0 refers to the primary camera.
   - 1, 2, etc., can be used if multiple cameras are connected.

3. ret, frame = cam.read()
   - ret is a boolean value (True/False) indicating whether the frame was captured successfully.
   - frame contains the actual image captured from the webcam.

4. cv2.imshow("webcam", frame)
   - The first argument is the window title.
   - The second argument is the image/frame to display.

5. cv2.waitKey(1)
   - Waits for 1 millisecond for a keyboard input.
   - Used to keep updating the video feed continuously.
   - 27 represents the ESC key, which is used to exit the program.

6. OpenCV uses BGR color format.

7. Horizontal Line:
   Y remains constant.

8. Vertical Line:
   X remains constant.

9. Rectangle:
   Requires top-left and bottom-right coordinates.

10. Circle:
   Requires center coordinates and radius.

11. putText():
   Used to display text on images.

12. Mediapipe allows to use real time tracking for gesture recognition or face recognition.

13. For hand identification there are 21 landmarks.

14. For the point to follow the index finger :
      - identify the frame shape like the height , width and the channels
      - similarly identify the index_finger points
      - to access the frame shape its in tuple so given by names like height , width and channels they can be accessed
      - multiply both for coordinates
      - a point with the help of cv2.circle() will follow your fingerpoints

15. MediaPipe returns coordinates in normalized form.
    - Values are between 0 and 1.
    - They are not actual screen coordinates.

16. To convert normalized coordinates into actual screen coordinates:

    x = int(index_finger.x * width)
    y = int(index_finger.y * height)

17. Landmark 8 represents the index finger tip.

18. A green dot can be made to follow the index finger using:
    cv2.circle(frame, (x,y), radius, colour, thickness)

19. If we draw directly on the frame, the drawing disappears because a new frame is generated continuously.

20. To make the drawing permanent, create a separate canvas:

    canvas = frame.copy() * 0

21. To combine the webcam feed and canvas:

    frame = cv2.add(frame, canvas)

22. Previous coordinates are required to draw continuous lines.

23. prev_x and prev_y store the previous position of the finger.

24. cv2.line(canvas, (prev_x, prev_y), (x,y), colour, thickness)
    draws a line between the previous and current finger positions.

25. MediaPipe landmarks used:
    - 8 : Index Finger Tip
    - 6 : Index Finger Joint
    - 12 : Middle Finger Tip
    - 10 : Middle Finger Joint

