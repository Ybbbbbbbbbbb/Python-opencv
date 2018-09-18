# _*_  coding: utf-8  _*_
# **************************************************
# @Author   : Ybbbbbbb
# @Time     : 2018-09-18 14:56
# @File     : example.py
# @SoftWare : PyCharm
# **************************************************

import cv2
import numpy as np

if __name__ == "__main__":
    example = cv2.imread("example.jpg",0)
    print(example.shape)
    cv2.imshow("example",example)


    kernal = cv2.getStructuringElement(cv2.MORPH_RECT,(3,3))
    eroded = cv2.erode(example,kernal)
    cv2.imshow("eroded",eroded)
    dilate = cv2.dilate(example,kernal)
    cv2.imshow("dilate",dilate)

    # 将两个图像相减，得到图像中的边缘部分
    dilate_erode = cv2.absdiff(dilate, eroded)
    cv2.imshow("dilate-erode",dilate_erode)
    cv2.imwrite("dilate-erode.jpg",dilate_erode,[int(cv2.IMWRITE_JPEG_QUALITY),95])
    print(dilate_erode)
    # 图像二值化
    val,result  = cv2.threshold(dilate_erode,60,255,cv2.THRESH_BINARY_INV)
    print(val)
    cv2.imshow("result",result)
    cv2.imwrite("result.jpg",result,[int(cv2.IMWRITE_JPEG_QUALITY),95])
    cv2.waitKey(0)
    cv2.destroyAllWindows()