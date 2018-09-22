# _*_  coding: utf-8  _*_
# **************************************************
# @Author   : Ybbbbbbb
# @Time     : 2018-09-22 13:59
# @File     : sharp.py
# @SoftWare : PyCharm
# **************************************************

import cv2
import numpy as np
from scipy import ndimage

dx = np.array([[-1, 0],
               [ 1, 0]])
dy = np.array([[0,-1],
               [0, 1]])

kernal = np.array([[0, -1, 0],
                   [-1, 5, -1],
                   [0, -1, 0]],dtype=np.float32)
kernal_2 = np.array([[-1, -1, -1],
                     [-1,  9, -1],
                     [-1, -1, -1]])
kernal_emboss = np.array([[1, 1, 0],
                          [1, 0, -1],
                          [0, -1, -1]])

kernal_edge = np.array([[-1, -1, -1],
                     [-1,  8, -1],
                     [-1, -1, -1]])
kernal_change = np.array([[0, 0, 0],
                          [0, 1, 0],
                          [0, 0, 0]])


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
cv2.imshow("origin", image)
image_b = cv2.split(image)[0]
image_g = cv2.split(image)[1]
image_r = cv2.split(image)[2]

# sharp_b = ndimage.convolve(image_b,kernal)
# sharp_g = ndimage.convolve(image_g,kernal)
# sharp_r = ndimage.convolve(image_r,kernal)
#
# sharp_image = cv2.merge([sharp_b, sharp_g, sharp_r])
# cv2.imshow("sharp",sharp_image)
#
# sharp_2b = ndimage.convolve(image_b,kernal_2)
# sharp_2g = ndimage.convolve(image_g,kernal_2)
# sharp_2r = ndimage.convolve(image_r,kernal_2)
# sharp_image2 = cv2.merge([sharp_2b, sharp_2g, sharp_2r])
# cv2.imshow("sharp_2", sharp_image2)

# emboss_image = ndimage.convolve(image_b, kernal_emboss)
# emboss_image = emboss_image + 128
# x = np.where(emboss_image > 255)
# print(x)
# cv2.imshow("emsboss", emboss_image)

# image_edgeb = ndimage.convolve(image_b, kernal_edge)
# image_edgeg = ndimage.convolve(image_g, kernal_edge)
# image_edger = ndimage.convolve(image_r, kernal_edge)
# image_edge = cv2.merge([image_edgeb,image_edgeg,image_edger])
# cv2.imshow("image_edgeb", image_edgeb)
# cv2.imshow("image_edge", image_edge)

image_b_change = ndimage.convolve(image_b, kernal_change)
image_g_change = ndimage.convolve(image_g, kernal_change)
image_r_change = ndimage.convolve(image_r, kernal_change)
image_change = cv2.merge([image_b_change, image_g_change, image_r_change])
cv2.imshow("change", image_change)


# image_sharp = cv2.filter2D(image, -1, kernal)
# cv2.imshow("filter_sharp", image_sharp)
#
# new_b = sharp(image_g)
# new_g = sharp(image_g)
# new_r = sharp(image_r)
#
# cv2.imshow("b",new_b)
# cv2.imshow('g',new_g)
# cv2.imshow("r",new_r)
#
# result = cv2.merge([new_b,new_g,new_r])
# cv2.imshow("origin", image)
# cv2.imshow("sharp", result)

if cv2.waitKey(0) == 27:
    cv2.destroyAllWindows()