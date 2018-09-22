# _*_  coding: utf-8  _*_
# **************************************************
# @Author   : Ybbbbbbb
# @Time     : 2018-09-20 9:09
# @File     : Gaussian_implement.py
# @SoftWare : PyCharm
# **************************************************

import numpy as np
import cv2
import math
from scipy import ndimage
def Gaussian(image, kernal): # 边界值使用0值填充方式
    n = kernal.shape[0] # 先得到滤波器的大小
    image_h = image.shape[0]
    image_w = image.shape[1]
    pad = int(n / 2)
    image_conv = np.zeros((image_h + 2 * pad, image_w + 2 * pad))

    image_conv[pad:-pad ,pad:-pad] = image
    result = np.zeros(image.shape,dtype=np.uint8) # 计算结果中会出现小数，在设置矩阵类型时设置为uint8
    for i in range(pad, image_h + pad):
        for j in range(pad, image_w + pad ):
            # test = image_conv[i-pad:i+pad+1,j-pad:j+pad+1]
            # print('test',str(test.shape),i,j)
            result[i-pad,j-pad] = np.sum(image_conv[i-pad:i+pad + 1,j-pad:j+pad + 1] * kernal)

    print(result)
    return result

def kernal_result(kernal_size,sigma): # 求出卷积核
    kernal = np.zeros((kernal_size,kernal_size))
    center = int(kernal_size / 2)
    for x in range(kernal_size):
        x_dis = pow(x - center, 2)
        for y in range(kernal_size):
            y_dis = pow(y - center, 2)
            kernal[x,y] = math.exp( -(x_dis + y_dis) /
                                    (2 * sigma ** 2) ) / (2 * math.pi * sigma**2)

    kernal = kernal / np.sum(kernal)

    return kernal


if __name__ == "__main__":
    image = cv2.imread("girl.jpg",0)
    kernal_size = 3 # 卷积核大小
    sigma = 18 # 高斯分布的方差

    kernal = kernal_result(kernal_size,sigma)

    gaussian_image = Gaussian(image,kernal=kernal)
    # 使用scipy中卷积操作
    gaussian_image_test = ndimage.convolve(image,kernal)

    cv2.imshow("true",image)
    cv2.imshow("test", gaussian_image)
    cv2.imshow("scipy",gaussian_image_test)

    if cv2.waitKey(0) == 27:
        print("高斯模糊完成")
        cv2.destroyAllWindows()


