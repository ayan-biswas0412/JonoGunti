import cv2 
import numpy as np
url = raw_input("Please enter the address of the IP webcam : ")
finalurl = "http://"+url+"/video"
cap = cv2.VideoCapture(finalurl)
while(True):
    ret, frame = cap.read()
    if frame is not None:
        cv2.imshow('frame',frame)
    q = cv2.waitKey(1)
    if q == ord("q"):
        break
cv2.destroyAllWindows()