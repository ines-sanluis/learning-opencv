import numpy as np
import cv2
from matplotlib import pyplot as plt

#Use matplotlib to zoom images, save it, etc

img = cv2.imread('IMD002.bmp', 0) #load an image in grayscale
plt.imshow(img, cmap = 'gray', interpolation = 'bicubic')
plt.xticks([]), plt.yticks([])  # to hide tick values on X and Y axis
plt.show()
