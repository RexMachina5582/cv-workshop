import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while(1):

    # Take each frame
    _, frame = cap.read()

    # Convert BGR to HSV
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # define range of blue color in HSV
    lower_blue = np.array([110,50,50])
    upper_blue = np.array([130,255,255])


    # Threshold the HSV image to get only blue colors
    blueMask = cv2.inRange(hsv, lower_blue, upper_blue)

    # Bitwise-AND mask and original image
    blueResult = cv2.bitwise_and(frame,frame, mask= blueMask)

    # Finding contours
    _, contours,hierarchy = cv2.findContours(blueMask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    cnt = contours[0]
    M = cv2.moments(cnt)
    cv2.drawContours(frame, contours,0, (255, 255, 255), cv2.FILLED,8,hierarchy);
    #cv2.rectangle(frame, cv2.boundingRect(contours[0]),  (0,255,0),2, 8,0);

    cv2.imshow('frame',frame)
    cv2.imshow('Bluemask',blueMask)
    cv2.imshow('blue',blueResult)
    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break

cv2.destroyAllWindows()
