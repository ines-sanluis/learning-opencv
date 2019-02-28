import numpy as np
import cv2

#Extract all pixels from the image which have values close to that of the green pixel
green = [40, 158, 16]
threshold = 40


img = cv2.imread('rubiks-cube.png', 1) #load in color
img_lab = cv2.cvtColor(img, cv2.COLOR_BGR2LAB)

lab = cv2.cvtColor(np.uint8([[green]]), cv2.COLOR_BGR2LAB)[0][0]
min_lab = np.array([lab[0] - threshold, lab[1] - threshold, lab[2] - threshold])
max_lab = np.array([lab[0] + threshold, lab[1] + threshold, lab[2] + threshold])
mask_lab = cv2.inRange(img_lab, min_lab, max_lab)

print("Min: ", min_lab)
print("Max: ", max_lab)

result_lab = cv2.bitwise_and(img_lab, img_lab, mask = mask_lab)
cv2.imshow("Output LAB", result_lab)
cv2.imshow("Input", img)
cv2.waitKey(0) #esperar a que o usuario pulse unha tecla
cv2.destroyAllWindows() #pechar a venta
