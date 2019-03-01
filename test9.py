import pandas as pd
import numpy as np
import cv2
import os

df = pd.read_csv("..\\Base de datos\\datamock.csv", sep=';')
data = df.values.tolist()
identificador = df.id.values.tolist()
diagnose = df.clinical_diagnosis.values.tolist()
file = open("data.dat", "a+")
index = 0

for i in range(1, 438):
    id = "IMD"+f"{i:03d}"
    path = "..\\Base de datos\\PH2 Dataset images\\"+id+"\\"
    img_src = path+id+"_Dermoscopic_Image\\"+id+".bmp"
    mask_src = path+id+"_lesion\\"+id+"_lesion.bmp"
    if os.path.isdir(path) is False: continue
    index += 1
    img = cv2.imread(img_src, 1)
    mask = cv2.imread(mask_src, 1)
    roi = cv2.bitwise_and(img, mask)
    banda_l = 0
    banda_a = 0
    banda_b = 0
    for r in range(0, roi.shape[0]):
        for c in range(0, roi.shape[1]):
            # if roi[r][c][0] == 0 and roi[r][c][1] == 0 and roi[r][c][2] == 0: continue
            lab = cv2.cvtColor(np.uint8([[roi[r][c]]]), cv2.COLOR_BGR2LAB)[0][0]
            banda_l += lab[0]
            banda_a += lab[1]
            banda_b += lab[2]
    banda_l = banda_l / img.size
    banda_a = banda_a / img.size
    banda_b = banda_b / img.size
    file.write(str(index)+" "+str(banda_l)+" "+str(banda_a)+" "+str(banda_b)+" "+diagnose[identificador.index(id)]+"\n")
