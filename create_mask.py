import cv2
import numpy as np
import sys

points = []
img1 = 'null'

def mouseHandler(event, x, y, flags, param):
    global points, img1
    if event == cv2.EVENT_LBUTTONDOWN:
        var = len(points)
        if var == 0: img1 = src.copy()
        point = (x, y)
        cv2.circle(img1, point, 2, (0, 0, 255), -1, 8, 0);
        points.append([x, y])
        if var >= 1:
            point_old = (points[var-1][0], points[var-1][1])
            cv2.line(img1, point_old, point, (0, 0, 255), 2, 8, 0);
        cv2.imshow('Imaxe', img1)

src = cv2.imread('images/IMD003.bmp')
cv2.namedWindow('Imaxe')
cv2.setMouseCallback('Imaxe', mouseHandler)
cv2.imshow('Imaxe', src)
while(1):
    k = cv2.waitKey(1) & 0xFF
    if k == ord('r'): #volver empezar
        points = []
        img1 = 'null'
        cv2.imshow('Imaxe', src)
    if k == ord('s'): #gardar
        array = np.array([points], dtype='int32')
        channel_count = src.shape[2]
        mask = np.zeros(src.shape, dtype=np.uint8)
        cv2.fillPoly(mask, array, (255,255,255))
        resultado = cv2.bitwise_and(src, mask)
        cv2.destroyWindow('Imaxe')
        cv2.imshow('Mascara', resultado)
        cv2.imwrite('mascara.png', resultado)
    elif k == 27:  #sair
        break

cv2.destroyAllWindows()
