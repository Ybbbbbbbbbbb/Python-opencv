# _*_  coding: utf-8  _*_
# **************************************************
# @Author   : Ybbbbbbb
# @Time     : 2018-09-17 19:47
# @File     : calcuAnddraw.py
# @SoftWare : PyCharm
# **************************************************

import cv2
import numpy as np
import matplotlib.pyplot as plt

# 计算并绘制直方图
def calanddraw(image,color):
    hist = cv2.calcHist([image],[0],None,[256],[0.0,255.0])
    # 使用plot函数绘图
    # plt.figure()
    # plt.plot(hist,color=color)
    # plt.xlabel([0,255])
    # plt.show()

    #  使用cv2的line画图
    minVal, maxVal, minLoc, maxLoc = cv2.minMaxLoc(hist) # 求出一维矩阵中的最大值，最小值，以及他们的索引
    print(maxVal)
    print(minVal)
    print(minLoc)
    print(maxLoc)
    histmap = np.zeros([256,256,3],dtype=np.uint8) #unit8 无符号类型，对应值域为0-255
    for i in range(256):
        intensity = int( hist[i] * int(0.9 * 256) / maxVal ) # 按照公式绘制图形
        cv2.line(histmap, (i,256), (i,256-intensity), color)
    return histmap



if __name__ == "__main__":
    image = cv2.imread("test.jpg", 1)
    b,g,r = cv2.split(image)
    image_b = calanddraw(b,[255,0,0])
    image_g = calanddraw(g,[0,255,0])
    image_r = calanddraw(r, [0,0,255])
    cv2.imshow("test",image)
    cv2.imshow("test_b",image_b)
    cv2.imshow("test_g",image_g)
    cv2.imshow("test_r",image_r)

    cv2.imwrite("blue.jpg",image_b,[int(cv2.IMWRITE_JPEG_QUALITY),95])
    cv2.imwrite("green.jpg",image_g,[int(cv2.IMWRITE_JPEG_QUALITY), 95])
    cv2.imwrite("red.jpg",image_r,[int(cv2.IMWRITE_JPEG_QUALITY), 95])
    cv2.waitKey(0)



    # 绘制均衡化直方图，只有灰度图
    image = cv2.imread("test.jpg",0)
    eq = cv2.equalizeHist(image)
    cv2.imshow("test",image)
    cv2.imshow("eq",eq)
    cv2.imwrite("equal_image.jpg",eq,[int(cv2.IMWRITE_JPEG_QUALITY), 95])
    cv2.waitKey(0)
    cv2.destroyAllWindows()
