# _*_  coding: utf-8  _*_
# **************************************************
# @Author   : Ybbbbbbb
# @Time     : 2018-09-25 14:29
# @File     : grayandBinary.py
# @SoftWare : PyCharm
# **************************************************

import cv2
import numpy as np
import matplotlib.pyplot as plt

image = cv2.imread("girl.jpg",1)
# cv2.imshow("origin", image)

binary_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
# cv2.imshow("binary", binary_image)
plt.figure(1)
plt.imshow(binary_image,cmap='gray')

ret, threshold1 = cv2.threshold(binary_image, 127, 255, type=cv2.THRESH_BINARY)
ret, threshold2 = cv2.threshold(binary_image, 100, 255, type= cv2.THRESH_BINARY_INV)
ret, threshold3 = cv2.threshold(binary_image, 127, 225, type=cv2.THRESH_TRUNC)
ret, threshold4 = cv2.threshold(binary_image, 127, 225, type=cv2.THRESH_TOZERO)
ret, threshold5 = cv2.threshold(binary_image, 127, 225, type=cv2.THRESH_TOZERO_INV)

images = [image,threshold1,threshold2,threshold3,threshold4,threshold5]
titles = ['origin','binary','binary_inv','trunc','tozero','tozero_inv']
plt.figure(2)
for i in range(6):
    plt.title(titles[i])
    plt.subplot(2,3,i+1)
    plt.imshow(images[i],cmap='gray')
    plt.xticks([])
    plt.yticks([])
plt.show()



cv2.imshow("thresh_binary", threshold3)


if cv2.waitKey(0) == 27:
    cv2.destroyAllWindows()