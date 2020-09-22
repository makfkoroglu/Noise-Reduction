import cv2
image=cv2.imread('image.png')
#image = cv2.resize(image, (350,350), interpolation = cv2.INTER_AREA)
blur=cv2.GaussianBlur(image, (5,5), 5)
output = cv2.medianBlur(image, ksize=3)
img_bilateral = cv2.bilateralFilter(blur, 13, 70, 100)
dst = cv2.fastNlMeansDenoisingColored(image,None,10,10,7,15)
cv2.imshow('Original Image',image)
cv2.imshow('Gaussian Image',blur)
cv2.imshow('Bilateral Image',img_bilateral)
cv2.imshow('Median',output)
cv2.imshow('dst',dst)
cv2.waitKey(0)
cv2.destroyAllWindows()
