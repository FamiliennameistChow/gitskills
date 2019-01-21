import cv2
import numpy as np

img = cv2.imread("timg.jpg", cv2.IMREAD_GRAYSCALE)
img = cv2.resize(img, (800, 600))
cv2.imshow("ii", img)
cv2.waitKey()

img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
img = cv2.GaussianBlur(img, (3, 3), 0, 0, cv2.BORDER_DEFAULT)
img_x = cv2.Sobel(img, cv2.CV_8U, 1, 0, ksize=3)

cv2.imshow("ii", img_x)
cv2.waitKey()

img_y = cv2.Sobel(img, cv2.CV_8U, 0, 1, ksize=3)
cv2.imshow("ii", img_y)
cv2.waitKey()
img = np.abs(img_x) + np.abs(img_y)

cv2.imshow("ii", img)
cv2.waitKey()

dilation = cv2.dilate(img, cv2.getStructuringElement(cv2.MORPH_RECT, (9, 7)), iterations=1)
cv2.imshow("ii", dilation)
cv2.waitKey()
img = cv2.erode(dilation, cv2.getStructuringElement(cv2.MORPH_RECT, (9, 1)), iterations=1)

cv2.imshow("ii", img)
cv2.waitKey()
