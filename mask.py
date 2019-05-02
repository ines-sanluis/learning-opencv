import cv2
import numpy as np
import sys

drag = False
flag = 0
points = []
img1 = 'null'

def mouseHandler(event, x, y, flags, param):
    global drag, flag, points, img1
    if event == cv2.EVENT_LBUTTONDOWN and drag == False:
        if flag == 0:
            var = len(points)
            if var == 0: img1 = src.copy()
            point = (x, y)
            cv2.circle(img1, point, 2, (0, 0, 255), -1, 8, 0);
            points.append([x, y])
            drag = True
            if var >= 1:
                point_old = (points[var-1][0], points[var-1][1])
                cv2.line(img1, point_old, point, (0, 0, 255), 2, 8, 0);
            cv2.imshow('Source image', img1)
    elif event == cv2.EVENT_LBUTTONUP and drag == True:
        cv2.imshow('Source image', img1)
        drag = False
    elif event == cv2.EVENT_RBUTTONDOWN:
        flag = 1
        img1 = src.copy()
        if len(points) != 0: cv2.polylines(img1, points, 1, (0,0,0), 2, 8, 0);
        cv2.imshow('Source image', img1)
    elif event == cv2.EVENT_RBUTTONUP:
        flag = len(points)
        array = np.array([points], dtype='int32')
        cv2.fillPoly(img1, pts=array, color=(255,255,255))
        cv2.imshow('Source image', img1)
        # roi = cv2.bitwise_and(img, mask)
    elif event == cv2.EVENT_MBUTTONDOWN:
        points = []
        drag = False
        flag = 0
        cv2.imshow('Source image', src)




src = cv2.imread('images/IMD003.bmp')
cv2.namedWindow('Source image')
cv2.setMouseCallback('Source image', mouseHandler)
cv2.imshow('Source image', src)
cv2.waitKey(0)
# while(1):
    # cv2.imshow('Source image', src)
    # k = cv2.waitKey(1) & 0xFF
    # if k == 27: break
