import numpy as np
import cv2
import os


# '''
# 读写图像
#
# '''
# img = np.zeros((3, 3), dtype=np.uint8)
# img = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)
# print(img.shape)

#
# '''
# imread()返回BGR格式图片
# 获取图像的属性
# imwrite()
# '''
# image = cv2.imread('000.png')
# print(image.shape)
# print(image.size)
# print(image.dtype)
# # cv2.imwrite('00.jpg', image)


# '''
# 生成图像
# np.random.randint(0,256,120000).reshape(400, 300)
# '''
# randomByteArray = bytearray(os.urandom(120000))
# grayImage = np.array(randomByteArray).reshape(300, 400)
# cv2.imwrite("RandomGray.png", grayImage)
# bgrImage = np.array(randomByteArray).reshape(100, 400, 3)
# cv2.imwrite("RandomColor.png", bgrImage)

# '''
# 使用np.array访问图像数据
# '''
# img = cv2.imread('000.png')
# img[20, 20] = [0, 0, 0]
# cv2.imshow("image", img)
# cv2.waitKey()


# '''
# numpy.array
# item()读取特定像素的数值
# itemset()改变特定图像的数值
# '''
# img = cv2.imread('00.jpg')
# print(img.item(150, 120, 0))
# img.itemset((150, 120, 0), 0)
# print(img.item(150, 120, 0))


# '''
# 操作某一通道的像素数值
# 使用数组索引
# '''
# img = cv2.imread('00.jpg')
# img[:, :, 1] = 0
# cv2.imshow("1", img)
# cv2.waitKey()


# '''
# 设置感兴趣区域(Region of Interest)
# 替换需要保证区域大小一直
# '''
# img = cv2.imread('00.jpg')
# my_roi = img[0:100, 0:100]
# img[300:400, 300:400] = my_roi
# cv2.imshow('1', img)
# cv2.waitKey()


