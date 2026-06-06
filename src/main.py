import cv2

#Open camera
cam = cv2.VideoCapture(0)


while True:
    ret, frame = cam.read()
    cv2.line(frame,(100,100),(300,100),(255,0,0),30)
    cv2.rectangle(frame,(100,100),(300,200),(0,255,255),10)
    cv2.circle(frame,(150,150),50,(0,0,255),3)
    cv2.putText(frame,"Air Canvas- Day 2",(50,50),3,1.5,(0,0,255),4)
    cv2.imshow("webcam",frame)
    if cv2.waitKey(1) == 27:
        break

cam.release()
cv2.destroyAllWindows()


