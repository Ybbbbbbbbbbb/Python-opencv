# _*_  coding: utf-8  _*_
# **************************************************
# @Author   : Ybbbbbbb
# @Time     : 2018-09-22 13:59
# @File     : sharp.py
# @SoftWare : PyCharm
# **************************************************

import cv2
import numpy as np

dx = np.array([[-1, 0],
               [ 1, 0]])
dy = np.array([[0,-1],
               [0, 1]])

kernal = np.array([[0, -1, 0],
                   [-1, 5, -1],
                   [0, -1, 0]],dtype=np.float32)

def sharp(image):
    W, H = image.shape
    # print(image.shape)
    result_x = np.zeros((W,H))
    result_y = np.zeros_like(image)
    result = np.zeros((W+2, H+2))
    print(result.shape)
    result[1:-1, 1:-1] = image
    new_image = np.zeros_like(image)
    for i in range(W):
        for j in range(H):
            result_x[i, j] = np.sum(result[i + 1:i + 3, j + 1:j + 3] * dx)
            result_y[i, j] = np.sum(result[i + 1:i + 3, j + 1:j + 3] * dy)
            new_image[i, j] = abs(result_x[i, j]) + abs(result_y[i, j])
    return new_image



image = cv2.imread("peixiuzhi.jpg",1)
image_b = cv2.split(image)[0]
image_g = cv2.split(image)[1]
image_r = cv2.split(image)[2]


image_sharp = cv2.filter2D(image, -1, kernal)
cv2.imshow("filter_sharp", image_sharp)

new_b = sharp(image_g)
new_g = sharp(image_g)
new_r = sharp(image_r)

cv2.imshow("b",new_b)
cv2.imshow('g',new_g)
cv2.imshow("r",new_r)

result = cv2.merge([new_b,new_g,new_r])
cv2.imshow("origin", image)
cv2.imshow("sharp", result)

if cv2.waitKey(0) == 27:
    cv2.destroyAllWindows()