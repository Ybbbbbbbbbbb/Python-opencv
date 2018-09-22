# _*_  coding: utf-8  _*_
# **************************************************
# @Author   : Ybbbbbbb
# @Time     : 2018-09-21 20:05
# @File     : canny_implement.py
# @SoftWare : PyCharm
# **************************************************

import cv2
import numpy as np
import math

image = cv2.imread("girl.jpg", 0)
cv2.imshow("origin", image)

# step_1 使用高斯滤波平滑图像
gau_image = cv2.GaussianBlur(image, (3,3), sigmaX=1.5)
cv2.imshow("gau_image", gau_image)


# step_2 计算梯度的增幅和方向
x,y = gau_image.shape
dx = np.array([[-1, -1],
               [1, 1]])
dy = np.array([[1, -1],
               [1, -1]])
grad_x = np.zeros((x-1, y-1))
grad_y = np.zeros((x-1, y-1))
improve_image = np.zeros((x-1, y-1))
for i in range(x-1):
    for j in range(y-1):
        grad_x[i, j] = np.sum(gau_image[i:i+2, j:j+2] * dx)
        grad_y[i, j] = np.sum(gau_image[i:i+2, j:j+2] * dy)
        improve_image[i, j] =  math.sqrt( grad_x[i,j] ** 2 + grad_y[i, j] ** 2)

cv2.imshow("improve_imamge", improve_image)

# step_3 非极大值抑制 NMS
w, h = improve_image.shape
NMS = np.copy(improve_image)
NMS[0,:] = NMS[w-1,:] = NMS[:,0] = NMS[:,h-1] = 0
for i in range(1, w-1):
    for j in range(1, h-1):
        if improve_image[i, j] == 0:
            NMS[i, j] = 0
        else:
            gradx = grad_x[i, j]
            grady = grad_y[i, j]
            gradtemp = improve_image[i, j]

            # 如果Y方向增幅值较大
            if abs(grady) > abs(gradx):
                weight = abs(gradx) / abs(grady)
                grad2 = improve_image[i-1, j]
                grad4 = improve_image[i+1, j]
                if gradx * grady > 0:
                    grad1 = improve_image[i-1, j-1]
                    grad3 = improve_image[i+1, j+1]
                else:
                    grad1 = improve_image[i-1, j+1]
                    grad3 = improve_image[i+1, j-1]

            # 如果x方向的增值较大
            else:
                weight = abs(grady) / abs(gradx)
                grad2 = improve_image[i-1, j]
                grad4 = improve_image[i+1, j]
                if abs(gradx) * abs(grady) > 0:
                    grad1 = improve_image[i+1, j-1]
                    grad3 = improve_image[i-1, j+1]
                else:
                    grad1 = improve_image[i-1 ,j+1]
                    grad3 = improve_image[i+1, j-1]
            dtemp1 = weight * grad1 + (1-weight) * grad2
            dtemp2 = weight * grad3 + (1 - weight) * grad4
            if gradtemp >= dtemp1 and gradtemp >= dtemp2:
                NMS[i, j] = gradtemp
            else:
                NMS[i, j] = 0

cv2.imshow("NMS",NMS)


# step_4 双阈值检测
w3, h3 = NMS.shape
dt = np.zeros((w3, h3))
tl = 0.1 * np.max(NMS)
th = 0.3 * np.max(NMS)

for i in range(1, w3-1):
    for j in range(1, h3-1):
        if NMS[i, j] < tl:
            dt[i, j] = 0
        elif NMS[i, j] > th:
            dt[i, j] = 1
        elif (NMS[i-1, j-1:j+1] < th).any() or (NMS[i, j-1:j+1] < th).any() or (NMS[i+1, j-1:j+1] < th).any():
            dt[i, j] = 1

cv2.imshow("final_result",dt)

if cv2.waitKey(0) == 27:
    cv2.destroyAllWindows()