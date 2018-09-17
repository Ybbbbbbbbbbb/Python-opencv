# _*_  coding: utf-8  _*_
# **************************************************
# @Author   : Ybbbbbbb
# @Time     : 2018-09-17 16:53
# @File     : access_image.py
# @SoftWare : PyCharm
# **************************************************

import cv2
import numpy as np


''''
image[i,j] = 255 灰度值
对于RGB图像来说，image[i,j,0]=255,image[i,j,1]=255,image[i,j,2]=255 是将图像某一点变为了黑色
'''

# 添加椒盐噪声
def add_salt(image,n):
    print(n)
    for number in range(n):
        i = int(np.random.random() * image.shape[0])
        j = int(np.random.random() * image.shape[1])
        if image.ndim == 2: # 灰度图像的ndim为 2，以此来判断图像是灰度还是RGB图像
            image[i,j] = 255
        elif image.ndim == 3:
            image[i,j,0] = 255
            image[i,j,1] = 255
            image[i,j,2] = 255
    return image

# 分离通道,合并通道
def split_channel(image):
    # opencv自带的split函数可以直接操纵RGB图像分离出通道值
    # b, g, r = cv2.split(image)
    # b = cv2.split(image)[0] # B通道
    # g = cv2.split(image)[1] # G通道
    # r = cv2.split(image)[2] # R通道

    # 使用numpy矩阵分离通道
    b = np.zeros(image.shape,dtype=image.dtype)
    g = np.zeros(image.shape,dtype=image.dtype)
    r = np.zeros(image.shape,dtype=image.dtype)
    b = image[:,:,0]
    g = image[:,:,1]
    r = image[:,:,2]

    cv2.imshow("red",r)
    cv2.imshow("green",g)
    cv2.imshow("blue",b)
    merged = cv2.merge([b,g,r])
    cv2.imshow("merge",merged)
    cv2.waitKey(1000)
    cv2.destroyAllWindows()



if __name__ == "__main__":
    image = cv2.imread("girl.jpg", 1)
    L,W,C = image.shape
    # n = min(L,W,C)
    print(image.ndim)
    print(image.shape)
    cv2.imshow("test", image)
    cv2.waitKey(1000)
    cv2.destroyAllWindows()

    # 调用加入椒盐噪声
    salt_image = add_salt(image,min(L,W))
    cv2.imshow("new_image",salt_image)
    cv2.waitKey(3000)
    cv2.destroyAllWindows()

    # 通道分离与合并
    split_channel(image)