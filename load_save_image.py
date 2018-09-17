# _*_  coding: utf-8  _*_
# **************************************************
# @Author   : Ybbbbbbb
# @Time     : 2018-09-17 9:05
# @File     : load_save_image.py
# @SoftWare : PyCharm
# **************************************************

import  cv2
import numpy as np


# 读取并显示图像
image = cv2.imread("girl.jpg", 1)
print(image.shape)
# 创建一个窗口
cv2.namedWindow("girl")
cv2.imshow("beauty",image)
# 使用imshow时必须加waitkey函数，不然不会显示图像
cv2.waitKey(10000)
cv2.destroyAllWindows()


# 创建、复制图像
image_2 = cv2.imread("test.jpg")
cv2.imshow("test",image_2)
cv2.waitKey(5000)

# 读取测试图片的大小
image2_size = np.zeros(image_2.shape,np.uint8)
print(image2_size.shape)

# 复制图片
new_image = image.copy()
print(new_image.shape)

# 写入图像
cv2.imwrite("E:\pycharm\opencv\peixiuzhi.jpg",image_2,[int(cv2.IMWRITE_JPEG_QUALITY),95])
'''
第三个参数针对特定的格式： 对于JPEG，其表示的是图像的质量，用0-100的整数表示，默认为95。
注意，cv2.IMWRITE_JPEG_QUALITY类型为Long，必须转换成int。
对于PNG，第三个参数表示的是压缩级别。cv2.IMWRITE_PNG_COMPRESSION，从0到9,压缩级别越高，图像尺寸越小。默认级别为3：
'''
