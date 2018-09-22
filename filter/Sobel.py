# _*_  coding: utf-8  _*_
# **************************************************
# @Author   : Ybbbbbbb
# @Time     : 2018-09-21 15:08
# @File     : Sobel.py
# @SoftWare : PyCharm
# **************************************************

import numpy as np
import cv2

sobel_x = np.array([[-1, 0, 1],
                    [-2, 0, 2],
                    [-1, 0, 1]])
sobel_y = np.array([[1, 2, 1],
                    [0, 0, 0],
                    [-1, -2, -1]])

def sobelX(image,sobel_x):
    x = image.shape[0]
    y = image.shape[1]
    sobel_image = np.zeros((x+2,y+2), dtype=np.uint8)
    sobel_image[1:-1,1:-1] = image
    result = np.zeros_like(image)
    for i in range(x):
        for j in range(y):
            result[i,j] = abs(np.sum(sobel_image[i:i+3,j:j+3] * sobel_x))
    return  result


def sobelY(image, sobel_y):
    x = image.shape[0]
    y = image.shape[1]
    sobel_image = np.zeros((x + 2, y + 2), dtype=np.uint8)
    sobel_image[1:-1, 1:-1] = image
    result = np.zeros_like(image)
    for i in range(x):
        for j in range(y):
            result[i, j] = abs(np.sum(sobel_image[i:i + 3, j:j + 3] * sobel_y))
    return result




image = cv2.imread("girl.jpg",0)
cv2.imshow("origin",image)
gaussian_image = cv2.GaussianBlur(image,(3,3),sigmaX=1.5)

image_x = sobelX(gaussian_image, sobel_x)
cv2.imshow("sobel_x", image_x)

image_y = sobelY(gaussian_image,sobel_y)
# cv2.imshow("sobel_y",image_y)

result = cv2.addWeighted(image_x,0.5,image_y,0.5,gamma=0)
cv2.imshow("final",result)

image_x_sobel = cv2.Sobel(gaussian_image,cv2.CV_16S,1,0)
image_y_sobel = cv2.Sobel(gaussian_image,cv2.CV_16S,0,1)
abX = cv2.convertScaleAbs(image_x_sobel)
abY = cv2.convertScaleAbs(image_y_sobel)
cv2.imshow("cv2_sobelX", abX)
# cv2.imshow("cv2_sobelY", abY)
cv_result = cv2.addWeighted(abX,0.5,abY,0.5,gamma=0)
cv2.imshow("cv_result",cv_result)

if cv2.waitKey(0) == 27:
    cv2.destroyAllWindows()
