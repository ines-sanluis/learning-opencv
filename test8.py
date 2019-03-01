import numpy as np
import cv2
import os
import xlrd

# file = ("..\\Base de datos\\PH2_dataset.xlsx")
file = ("..\\Base de datos\\mock.xlsx")
wb = xlrd.open_workbook(file)
sheet_names = wb.sheet_names()
sheet = wb.sheet_by_name(sheet_names[0])
for f in range (1, 201):
    fila = sheet.row(f)
    if "IMD002" in fila.value:
        print(fila)
    # print(fila[0], fila[1])

# for i in range(1, 438):
# print(sheet.cell_value(0, 0))
# for i in range(1, 3):
    # id = "IMD"+f"{i:03d}"
    # path = "..\\Base de datos\\PH2 Dataset images\\"+id+"\\"
    # img_src = path+id+"_Dermoscopic_Image\\"+id+".bmp"
    # mask_src = path+id+"_lesion\\"+id+"_lesion.bmp"
    # if os.path.isdir(path) is False: continue
    # img = cv2.imread(img_src, 1)

    # mask = cv2.imread(mask_src, 1)
    # roi = cv2.bitwise_and(img, mask)
