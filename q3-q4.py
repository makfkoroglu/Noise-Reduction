import cv2
import numpy as np
image=cv2.imread('g.jfif',0)
#Oimage = cv2.resize(image, (350,350), interpolation = cv2.INTER_AREA)
kernel_5x5 = np.ones((5, 5), np.float32) / 25
kernel_sharpen_3 = np.array([[-1,-1,-1,-1,-1],
                             [-1, -1, -1, -1,-1],
                             [-1, -1, 24, -1,-1],
                             [-1, -1, -1, -1,-1],
                             [-1,-1,-1,-1,-1]])
output = cv2.filter2D(image, -1, kernel_5x5)
output2 = cv2.filter2D(image, -1, kernel_sharpen_3)
#cv2.imshow('original',image)
#cv2.imshow('Low-Pass Filter',output)
cv2.imshow('High-Pass Filter',output2)
cv2.waitKey(0)
cv2.destroyAllWindows()