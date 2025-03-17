import cv2
import numpy as np
def get_limits(colour):
    c=np.uint8([[colour]])
    hsv = cv2.cvtColor(c,cv2.COLOR_BGR2HSV)

    lower_Limit=hsv[0][0][0]-10,100,100
    upper_Limit=hsv[0][0][0]+10,255,255
    lower_Limit=np.array(lower_Limit,dtype=np.uint8)
    upper_Limit=np.array(upper_Limit,dtype=np.uint8)
    return lower_Limit,upper_Limit