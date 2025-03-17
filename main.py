import cv2
import numpy as np
from PIL import Image
from util import get_limits
url = 'http://10.5.126.236:8080/video'  

# Open the video stream
cap = cv2.VideoCapture(url)
yellow=[0,255,255]

while True:
    _, frame = cap.read()
    hsvimage=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    lower_Limit,upper_Limit=get_limits(yellow)
    mask=cv2.inRange(hsvimage,lower_Limit,upper_Limit)
    mask_=Image.fromarray(mask)
    bbox=mask_.getbbox()
    if bbox is not None:
        xi,y1,x2,y2=bbox
        frame=cv2.rectangle(frame,(xi,y1),(x2,y2),(0,255,0),2)
    print(bbox)
    cv2.imshow('frame', frame)
   
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()