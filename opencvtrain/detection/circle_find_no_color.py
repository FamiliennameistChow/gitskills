# -*- coding: utf-8 -*-
import cv2
import numpy as np
import sys
import os
import math
import matplotlib.pyplot as plt


def unevenLightCompensate(img, blockSize):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    average = np.mean(gray)

    rows_new = int(np.ceil(gray.shape[0] / blockSize))
    cols_new = int(np.ceil(gray.shape[1] / blockSize))

    blockImage = np.zeros((rows_new, cols_new), dtype=np.float32)
    for r in range(rows_new):
        for c in range(cols_new):
            rowmin = r * blockSize
            rowmax = (r + 1) * blockSize
            if (rowmax > gray.shape[0]):
                rowmax = gray.shape[0]
            colmin = c * blockSize
            colmax = (c + 1) * blockSize
            if (colmax > gray.shape[1]):
                colmax = gray.shape[1]

            imageROI = gray[rowmin:rowmax, colmin:colmax]
            temaver = np.mean(imageROI)
            blockImage[r, c] = temaver

    blockImage = blockImage - average
    blockImage2 = cv2.resize(blockImage, (gray.shape[1], gray.shape[0]), interpolation=cv2.INTER_CUBIC)
    gray2 = gray.astype(np.float32)
    dst = gray2 - blockImage2
    dst = dst.astype(np.uint8)
    dst = cv2.GaussianBlur(dst, (3, 3), 0)
    dst = cv2.cvtColor(dst, cv2.COLOR_GRAY2BGR)

    return dst


def calcGrayHist(I):
    # 计算灰度直方图
    h, w = I.shape[:2]
    grayHist = np.zeros([256], np.uint64)
    for i in range(h):
        for j in range(w):
            grayHist[I[i][j]] += 1
    return grayHist


# 数据平滑
def moving_average(interval, window_size):
    window = np.ones(int(window_size)) / float(window_size)
    return np.convolve(interval, window, 'same')


def detecte_circle(img):

    img2 = img.copy()
    print(img.shape)
    # cv2.imshow('img', img)


    img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    h, s, v =cv2.split(img)

    cv2.imshow('h', h)
    # cv2.waitKey()
    # cv2.destroyAllWindows()

    cv2.imshow('s', s)
    cv2.waitKey()
    cv2.destroyAllWindows()

    cv2.imshow('v', v)
    # cv2.waitKey()
    # cv2.destroyAllWindows()

    img_1 = cv2.subtract(h, s)
    cv2.imshow('h-s', img_1)
    img_2 = cv2.subtract(v, s)
    cv2.imshow('v-s', img_2)
    img_3 = cv2.subtract(h, v)
    cv2.imshow('h-v', img_3)
    # cv2.waitKey()
    # cv2.destroyAllWindows()

    fi = s / 255.0
    gamma = 1.4
    img_gamma = (np.power(fi, gamma) * 255.0).astype(np.uint8)
    cv2.imshow('img_gamma', img_gamma)  # opencv只支持float32的图像显示和操作，然后float64是numpy的数据类型，opencv中不支持
    # grayHist = calcGrayHist(img_gamma)
    # x = np.arange(256)
    hist = cv2.calcHist([img_gamma], [0], None, [256], [0, 256])
    hist_av = moving_average(interval=hist.reshape(-1), window_size=5)  # 数据平滑
    # # 求直方图极值  ##

    # 将多维数组降位一维 numpy.ravel()返回视图，在原图操作  与numpy.flatten()返回拷贝，对原图没影响
    # plt.hist(img_gamma.flatten(), 256, [0, 256])
    # plt.plot(hist)
    # plt.plot(hist_av)
    # plt.show()

    # cv2.waitKey()
    # cv2.destroyAllWindows()

    # img = unevenLightCompensate(img, 11)
    # cv2.imshow('img_1', img)
    # cv2.waitKey()
    # cv2.destroyAllWindows()
    # print(img.shape)


    # gary = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # cv2.imshow('gary', gary)
    # cv2.waitKey()
    # cv2.destroyAllWindows()

    # img_at_mean = cv2.adaptiveThreshold(gary, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY_INV, 5, 10)
    img_at_mean = cv2.adaptiveThreshold(s, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 161, 5)
    # _, img_at_mean = cv2.threshold(gary, 150, 255, cv2.THRESH_BINARY_INV)

    cv2.imshow('img', img_at_mean)
    cv2.waitKey()
    cv2.destroyAllWindows()
    print(img_at_mean.shape)


    kernel_1 = np.ones((5, 5), np.uint8)
    dilation_1 = cv2.dilate(img_at_mean, kernel_1)
    cv2.imshow('dilation_1', dilation_1)
    # cv2.waitKey()
    # cv2.destroyAllWindows()

    # kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5))  # 定义结构元素
    # closing = cv2.morphologyEx(dilation_1
    # , cv2.MORPH_CLOSE, kernel)  # 闭运算
    #
    # cv2.imshow('closing', closing)
    # cv2.waitKey()
    # cv2.destroyAllWindows()
    #
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))  # 定义结构元素
    opening = cv2.morphologyEx(dilation_1, cv2.MORPH_OPEN, kernel)  # 开运算

    cv2.imshow('opening', opening)
    # cv2.waitKey()
    # cv2.destroyAllWindows()

    img_median = cv2.medianBlur(dilation_1, 5)
    cv2.imshow('img_median', img_median)
    # cv2.waitKey()
    # cv2.destroyAllWindows()

    # dilation = cv2.dilate(img_median, kernel_1)
    # img_at_mean = img_at_mean[10:img_at_mean.shape[0]-10, 10:img_at_mean.shape[1]-10]

    contours, hierarchy = cv2.findContours(dilation_1, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)

    print("contours length:", len(contours))

    for contour in contours:
        area = cv2.contourArea(contour)
        length = cv2.arcLength(contour, True)
        if area < 1000 or length < 100:
            continue
        if (length*length/area) >= 4 * 3 and (length*length/area) <= 4 * 5:
            img_contours = cv2.drawContours(img2, [contour], 0, (0, 255, 0), 1)
            cv2.imshow('contours', img_contours)
            # cv2.waitKey()
            # cv2.destroyAllWindows()


    # circles = cv2.HoughCircles(img_at_mean, cv2.HOUGH_GRADIENT, 1, 100, param1=100, param2=30)
    # print(circles)
    #
    # try:
    #     print("number of circles", len(circles[0]))
    #     for circle in circles[0]:
    #         x = int(circle[0])
    #         y = int(circle[1])
    #         r = int(circle[2])
    #         print("x", x)
    #         print("y", y)
    #         print("r", r)
    #         img = cv2.circle(img, (x, y), r, (255, 0, 0), 1)
    #
    #     cv2.imshow("res", img)
    #     cv2.waitKey()
    #     cv2.destroyAllWindows()
    #
    # except TypeError:
    #     print("no circles found!!")


dir = os.path.join(sys.path[0], "data", "1.png")
img = cv2.imread(dir)
detecte_circle(img)

# # # # ******** 摄像头获取图片************
# videoCaputer = cv2.VideoCapture(0)
# # # videoCaputer.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)  # 1920
# # # videoCaputer.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)  # 1080
# #
# while True:
#     _, frame = videoCaputer.read()
#     print(frame.shape)
#     cv2.imshow("test", frame)
#     if cv2.waitKey(1) == 27:
#         break
#     detecte_circle(frame)
# videoCaputer.release()
# cv2.destroyAllWindows()