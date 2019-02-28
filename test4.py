import numpy as np
import cv2

img = cv2.imread('IMD002.bmp', 1) #load in color
img_lab = cv2.cvtColor(img, cv2.COLOR_BGR2LAB)
# cv2.imshow('Imaxe', img_lab) #titulo da imaxe e fonte
cv2.imshow('Imaxe', img) #titulo da imaxe e fonte
cv2.waitKey(0) #esperar a que o usuario pulse unha tecla
cv2.destroyAllWindows() #pechar a venta
