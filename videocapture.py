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

    # define range of green color in HSV
    lower_green = np.array([50,50,50])
    upper_green = np.array([70,255,255])

    # Threshold the HSV image to get only blue colors
    blueMask = cv2.inRange(hsv, lower_blue, upper_blue)
    greenMask = cv2.inRange(hsv, lower_green, upper_green)

    # Bitwise-AND mask and original image
    blueResult = cv2.bitwise_and(frame,frame, mask= blueMask)
    greenResult = cv2.bitwise_and(frame,frame, mask= greenMask)

    cv2.imshow('frame',frame)
    cv2.imshow('Bluemask',blueMask)
    cv2.imshow('Greenmask',greenMask)
    cv2.imshow('blue',blueResult)
    cv2.imshow('green',greenResult)
    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break

cv2.destroyAllWindows()
