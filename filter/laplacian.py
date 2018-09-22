# _*_  coding: utf-8  _*_
# **************************************************
# @Author   : Ybbbbbbb
# @Time     : 2018-09-21 16:33
# @File     : laplacian.py
# @SoftWare : PyCharm
# **************************************************

import cv2
import numpy as np

lap = np.array([[0, 1, 0],
                [1, -4, 1],
                [0, 1, 0]])  # laplacian算子

def laplacian(image,lap):
    x = image.shape[0]
    y = image.shape[1]
    result = np.zeros_like(image,dtype=np.uint8)
    lap_image = np.zeros((x+2,y+2))
    lap_image[1:-1,1:-1] = image
    for i in range(x):
        for j in range(y):
            result[i,j] = np.sum(lap_image[i:i+3,j:j+3] * lap)

    return result




image = cv2.imread("girl.jpg",0)
cv2.imshow("image",image)
gau_image = cv2.GaussianBlur(image,(3,3),sigmaX=1.5)
lap_image = laplacian(gau_image,lap)
cv2.imshow("lap_image",lap_image)

if cv2.waitKey(0) == 27:
    cv2.destroyAllWindows()
