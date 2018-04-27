import numpy as np
import cv2

img = np.zeros((512,512,3),np.uint8)

cv2.ellipse(img,(200,200),(80,50),0,0,360,(0,255,0),-1)
cv2.ellipse(img,(200,200),(80,50),45,0,360,(0,0,255),1)

cv2.imshow("img",img)
cv2.waitKey(0)