import os
import cv2
from collections import defaultdict
import numpy as np

dir = "./ds_2018_0809"
i = 101
filecount = len(os.listdir(dir))
in_png = "label_" + str(i) + ".png"
in_file = os.path.join(dir, in_png)

dic = defaultdict(list)
im = cv2.imread(in_file, cv2.IMREAD_UNCHANGED)
for i in range(im.shape[0]):
    for j in range(im.shape[1]):
        value = im[i, j]
        dic[value[0]].append((i, j))

print(in_file)
print(dic, im.shape)