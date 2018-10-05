import cv2
import numpy as np


# img = cv2.imread('ACP.PNG', cv2.IMREAD_COLOR)
# gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# edges = cv2.Canny(gray, 50, 120)
# minLineLength = 20
# maxLineGap = 5
# lines = cv2.HoughLinesP(edges, 1, np.pi/180, 100, minLineLength, maxLineGap)
# for x1, y1, x2, y2 in lines[0]:
#     cv2.line(img, (x1, y1), (x2, y2), (0, 255, 0), 2)
#
# cv2.imshow('edges', edges)
# cv2.imshow('lines', img)
# cv2.waitKey()
# cv2.destroyAllWindows()


# ****绘制直线******##
img = np.zeros((512, 512, 3), np.uint8)
cv2.line(img, (0, 0), (511, 511), (255, 0, 0), 5)
cv2.imshow("img", img)
cv2.waitKey()