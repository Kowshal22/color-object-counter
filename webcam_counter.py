import numpy as np
import os
import cv2
from PIL import Image
from func import get_color

img=cv2.imread(os.path.join(os.getcwd(),'pictures','king.jpg'))
orange=[0,165,255]
webimg = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
lower, upper = get_color(color=orange)
mask = cv2.inRange(webimg, lower, upper)
kernel = np.ones((5, 5), np.uint8)
mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)
contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
filtered_contours = [cnt for cnt in contours if cv2.contourArea(cnt) > 1]
for cnt in filtered_contours:
    x1,y1,w,h = cv2.boundingRect(cnt)
    cv2.rectangle(img, (x1, y1), (x1+w,y1+h),[0,165.255] ,5)
count=len(filtered_contours)
cv2.putText(img,f"count={count}",(1,100),cv2.FONT_HERSHEY_PLAIN,5,[0,0,255],2)
cv2.namedWindow("Color object counter", cv2.WND_PROP_FULLSCREEN)
cv2.setWindowProperty("Color object counter", cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
cv2.imshow("Color object counter", img)
cv2.waitKey(0)
cv2.destroyAllWindows()