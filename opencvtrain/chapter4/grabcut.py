import numpy as np
import cv2
from matplotlib import pyplot as plt

img = cv2.imread('gg.jpg')
mask = np.zeros(img.shape[:2], np.uint8)

bgdModel = np.zeros((1, 65), np.float64)
fgdModel = np.zeros((1, 65), np.float64)

rect = (172, 38, 1120, 787)  # 划定区域
# 函数返回值为mask,bgdModel,fgdModel
cv2.grabCut(img, mask, rect, bgdModel, fgdModel, 5, cv2.GC_INIT_WITH_RECT)

mask2 = np.where((mask == 2)|(mask == 0), 0, 1).astype('uint8') # 使用0和2做背景
img = img*mask2[:, :, np.newaxis]

plt.subplot(121), plt.imshow(img) # 使用蒙板来获取前景区域
plt.title('grabcut'), plt.xticks([]), plt.yticks([])
plt.subplot(122), plt.imshow(cv2.cvtColor(cv2.imread('gg.jpg'), cv2.COLOR_BGR2RGB))
plt.title("original"), plt.xticks([]), plt.yticks([])
plt.show()
# print(img.shape)