import cv2
import numpy
import scipy.interpolate

im = cv2.imread('gg.jpg', cv2.IMREAD_COLOR)
img = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
cv2.imshow('gray', img)
cv2.waitKey()
