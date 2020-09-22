import cv2
import numpy as np
img = cv2.imread('g.png',0)
img=cv2.resize(img,(450,650),interpolation = cv2.INTER_AREA)
cv2.imwrite('resize.png',img)
kernel = np.ones((3,3), np.uint8)
edges = cv2.Canny(img,0,80)

#cv2.imshow("Image", img)
#img_erosion = cv2.erode(edges, kernel, iterations=1) 
#img_dilation = cv2.dilate(edges, kernel, iterations=1) 
#cv2.imshow('Erosion', img_erosion) 
#cv2.imshow('Dilation', img_dilation)
cv2.imshow("Edge Detected Image", edges)
cv2.imwrite('gg.png',edges)
cv2.waitKey(0) # waits until a key is pressed
cv2.destroyAllWindows() 
