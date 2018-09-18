# _*_  coding: utf-8  _*_
# **************************************************
# @Author   : Ybbbbbbb
# @Time     : 2018-09-18 14:24
# @File     : morphology.py
# @SoftWare : PyCharm
# **************************************************

import numpy as np
import cv2

# 定义结构化元素 MORPH_CROSS指的是十字形,还有许多其他的形状
element = cv2.getStructuringElement(cv2.MORPH_CROSS, (3, 3))
print(element)


# 首先定义卷积核
kernal = cv2.getStructuringElement(cv2.MORPH_RECT,(3,3))
image = cv2.imread("test.dib")
cv2.imshow("struct", image)

# 显示腐蚀图像
eroded = cv2.erode(image,kernal)
cv2.imshow("erode",eroded)

# 显示膨胀图像
dilated = cv2.dilate(image, kernal)
cv2.imshow("dilate",dilated)
cv2.waitKey(0)
cv2.destroyAllWindows()


# 显示开运算图像(先腐蚀在膨胀)
opened = cv2.morphologyEx(image,cv2.MORPH_OPEN,kernal)
cv2.imshow("opened",opened)

# 显示闭运算图像(想膨胀在腐蚀)
closed = cv2.morphologyEx(image,cv2.MORPH_CLOSE,kernal)
cv2.imshow("closed",closed)

final = cv2.morphologyEx(opened,cv2.MORPH_CLOSE,kernal)
cv2.imshow("open+close",final)
cv2.waitKey(10000)
cv2.destroyAllWindows()
