import cv2
import numpy as np
from scipy import ndimage
from matplotlib import pyplot as plt

# '''
# ###########################高通滤波器##########################
# '''
# kernel_3x3 = np.array([[-1, -1, -1],
#                        [-1, 8, -1],
#                        [-1, -1, -1]])
#
# kernel_5x5 = np.array([[-1, -1, -1, -1, -1],
#                        [-1,  1,  2,  1, -1],
#                        [-1,  2,  4,  2, -1],
#                        [-1,  1,  2,  1, -1],
#                        [-1, -1, -1, -1, -1]])
#
# img = cv2.imread('ACP.PNG', cv2.IMREAD_GRAYSCALE)
#
# k3 = ndimage.convolve(img, kernel_3x3)
# k5 = ndimage.convolve(img, kernel_5x5)
#
# blurred = cv2.GaussianBlur(img, (17, 17), 0)
# g_hpf = img - blurred
#
# cv2.imshow('3*3', k3)
# cv2.imshow('5*5', k5)
# cv2.imshow('g_hpf', g_hpf)
# cv2.imshow('1', img)
# cv2.waitKey()


# '''
# ##########################边缘检测#################################
# '''
# # ***********************canny 边缘检测*************************** #
# '''
# cv2.Canny()  第一个参数是输入图像，第二个和第三个参数是maxVal和minVal
# '''
# img = cv2.imread("ACP.PNG", cv2.IMREAD_GRAYSCALE)
# cv2.imwrite('canny.png', cv2.Canny(img, 200, 300))
# im = cv2.imread('canny.png', cv2.IMREAD_GRAYSCALE)
# plt.subplot(121), plt.imshow(im, cmap='gray')
# plt.title('canny png')
# plt.subplot(122), plt.imshow(img, cmap='gray')
# plt.title('original png')
# plt.show()


# '''
# ##########################轮廓检测#################################
# ## 固定阈值二值化
# ret, dst = cv2.threshold(src, thresh, maxval, type)
# src： 输入图，只能输入单通道图像，通常来说为灰度图
# dst： 输出图
# thresh： 阈值
# maxval： 当像素值超过了阈值（或者小于阈值，根据type来决定），所赋予的值
# type：二值化操作的类型，包含以下5种类型： cv2.THRESH_BINARY； cv2.THRESH_BINARY_INV； cv2.THRESH_TRUNC； cv2.THRESH_TOZERO；cv2.THRESH_TOZERO_INV
#
# '''
#
# img = np.ones((200, 200), dtype=np.uint8)
# img[50:150, 50:150] = 255
# ret, thresh = cv2.threshold(img, 127, 255, 0)
# image, contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
# color = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)
# img = cv2.drawContours(color, contours, -1, (0, 255, 0), 2)
# cv2.imshow('contours', img)
# cv2.waitKey()


# '''
# ######################通道拆分与通道合并#######################
# cv2.split（）
# cv2.split函数分离出的B、G、R是单通道图像
# (B, G, R) = cv2.split(im)  or
# b = cv2.split(img)[0]
# g = cv2.split(img)[1]
# r = cv2.split(img)[2]
# cv2.merge()
# '''
# im = cv2.imread("ACP.PNG", cv2.IMREAD_COLOR)
# print(im.ndim)
# (B, G, R) = cv2.split(im)  # B = im[:, :, 0]; G = im[:, :, 1]; R = im[:, :, 2]
#
# # print(B)
#
# print("original shape:%s, r shape:%s" % (im.shape, R.shape))
# cv2.imshow("original", im)
# cv2.imshow("red", R)
# cv2.imshow("Green", G)
# cv2.imshow("BLue", B)
# cv2.waitKey()
# # **************cv2.merge()******************* #
# zeros = np.zeros(im.shape[:2], dtype=np.uint8)
# # print(zeros)
# cv2.imshow("Blue", cv2.merge([B, zeros, zeros]))
# cv2.imshow("Green", cv2.merge([zeros, G, zeros]))
# cv2.imshow("Red", cv2.merge([zeros, zeros, R]))
# cv2.waitKey()
