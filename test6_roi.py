import numpy as np
import cv2

img = cv2.imread('IMD002.bmp', 1) #load in color
r = cv2.selectROI(img)
img_cropped = img[int(r[1]):int(r[1]+r[3]), int(r[0]):int(r[0]+r[2])]
cv2.imshow("Image", img_cropped)
cv2.waitKey(0)
cv2.destroyAllWindows()
