import numpy as np
import os
import cv2
from PIL import Image
from func import get_color

webcam = cv2.VideoCapture(0)
yellow=[0,255,255]
while True:
    ret, frame = webcam.read()
    webimg = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    lower, upper = get_color(color=yellow)
    mask = cv2.inRange(webimg, lower, upper)
    contours,_=cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    filtered_contours = [cnt for cnt in contours if cnt is not None and len(cnt) > 0 and cv2.contourArea(cnt) > 500]
    for cnt in filtered_contours:
        x1,y1,w,h = cv2.boundingRect(cnt)
        cv2.rectangle(frame, (x1, y1), (x1+w,y1+h),[0,165.255] ,5)
    count=len(filtered_contours)
    cv2.putText(frame,f"count={count}",(1,100),cv2.FONT_HERSHEY_PLAIN,5,[0,0,255],2)
    cv2.namedWindow("Color object counter", cv2.WND_PROP_FULLSCREEN)
    cv2.setWindowProperty("Color object counter", cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
    cv2.imshow("Color object counter", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
webcam.release()
cv2.destroyAllWindows()