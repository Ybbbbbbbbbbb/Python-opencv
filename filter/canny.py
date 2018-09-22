# _*_  coding: utf-8  _*_
# **************************************************
# @Author   : Ybbbbbbb
# @Time     : 2018-09-19 19:27
# @File     : canny.py
# @SoftWare : PyCharm
# **************************************************

import cv2
import numpy as np

def canny_change(minthreshold):
    detected_edges = cv2.GaussianBlur(image_split, (3, 3), 0)
    canny_image = cv2.Canny(detected_edges,minthreshold, minthreshold*3,apertureSize=3)
    # canny_image = cv2.bitwise_and(image, image, mask=canny_image)  # just add some colours to edges from original image.
    cv2.imshow("change_canny",canny_image)



image = cv2.imread("girl.jpg")
image_split = cv2.split(image)[0]
minthreshold = 0
maxthreshold = 200

cv2.namedWindow("change_canny")
cv2.createTrackbar("canny_mage","change_canny",minthreshold,maxthreshold,canny_change)

canny_change(0) # 初始化


if cv2.waitKey(0) == 27:
    cv2.destroyAllWindows()
