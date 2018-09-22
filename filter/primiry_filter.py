# _*_  coding: utf-8  _*_
# **************************************************
# @Author   : Ybbbbbbb
# @Time     : 2018-09-18 16:46
# @File     : primiry_filter.py
# @SoftWare : PyCharm
# **************************************************

import cv2
import numpy as np

image = cv2.imread("peixiuzhi.jpg",1)
cv2.imshow("test",image)
print(image.shape)

# smooth_result = cv2.blur(image,(10,10))
# cv2.imshow("smooth_result",smooth_result)

#
#
# gaussion_result = cv2.GaussianBlur(image,(25,25),2)
# cv2.imshow("test_2",gaussion_result)
#
# # Sobel
# x = cv2.Sobel(gaussion_result,cv2.CV_16S,1,0)
# y = cv2.Sobel(gaussion_result,cv2.CV_16S,0,1)
#
# absX = cv2.convertScaleAbs(x) #转回uint8
# absY = cv2.convertScaleAbs(y)
#
# dist = cv2.addWeighted(absX,0.5,absY,0.5,0)
# cv2.imshow("Sobel_result",dist)

access_image = cv2.GaussianBlur(image,(25,25),2)
lap_imgae = cv2.Laplacian(access_image,cv2.CV_16S,ksize=3)
image_result = cv2.convertScaleAbs(lap_imgae)
cv2.imshow("laplacian",image_result)

cv2.waitKey(0)
cv2.destroyAllWindows()