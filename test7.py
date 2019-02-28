import numpy as np
import cv2

img = cv2.imread('IMD002.bmp', 1)
mask = cv2.imread('IMD002_lesion.bmp', 1)
roi = cv2.bitwise_and(img, mask)

banda_l = 0
banda_a = 0
banda_b = 0

for r in range(0, roi.shape[0]):
    for c in range(0, roi.shape[1]):
        lab = cv2.cvtColor(np.uint8([[roi[r][c]]]), cv2.COLOR_BGR2LAB)[0][0]
        banda_l += lab[0]
        banda_a += lab[1]
        banda_b += lab[2]

banda_l = banda_l / img.size
banda_a = banda_a / img.size
banda_b = banda_b / img.size

print("Banda L: ",banda_l)
print("Banda a: ",banda_a)
print("Banda b: ",banda_b)
print("Valor:\n", banda_l, banda_a, banda_b)

# cv2.imshow("Imaxe", roi)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
