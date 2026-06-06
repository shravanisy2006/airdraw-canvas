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

12. OpenCV directly modifies the frame before displaying it.

