# _*_  coding: utf-8  _*_
# **************************************************
# @Author   : Ybbbbbbb
# @Time     : 2018-10-29 21:46
# @File     : kalmanfilter.py
# @SoftWare : PyCharm
# **************************************************

import cv2
import numpy as np

""""
使用卡尔曼滤波做一个鼠标跟踪程序
"""


# 定义一个空的画图区域
frame = np.zeros((700, 700, 3), np.uint8)

# 初始化测量坐标和鼠标运动预测的数组
last_measurement = current_measurement = np.array((2, 1), np.float32)
last_prediction = current_prediction = np.zeros((2, 1), np.float32)

kalman = cv2.KalmanFilter(4, 2) # 4:状态数，包括(x,y,dx,dy)鼠标的位置及速度。 2:代表的是观测值，也就是坐标
kalman.measurementMatrix = np.array([[1, 0, 0, 0], [0, 1, 0, 0]], dtype=np.float32) # H 系统测量矩阵
kalman.processNoiseCov = np.array([[1, 0, 0, 0],[0, 1, 0, 0],[0, 0, 1, 0],[0, 0, 0, 1]], dtype=np.float32) * 0.5  # 系统误差
kalman.transitionMatrix = np.array([[1, 0, 1, 0], [0, 1, 0, 1], [0, 0, 1, 0], [0, 0, 0, 1]], np.float32) # A 状态转移矩阵

# 定义鼠标回调函数
def mousemove(event, x, y, s, p):
    global frame, current_measurement, measurements, last_measurement, current_prediction, last_prediction
    last_prediction = current_prediction # 把当前的预测作为上一次的预测
    last_measurement = current_measurement # 把当前的测量作为上一次的测量
    current_measurement = np.array([[np.float32(x)], [np.float32(y)]]) # 当前测量
    kalman.correct(current_measurement) # 修正卡尔曼滤波值
    current_prediction = kalman.predict()  # 预测得到下一步的位置

    lmx, lmy = last_measurement[0], last_measurement[1]  # 上一次测量坐标
    cmx, cmy = current_measurement[0], current_measurement[1]  # 当前测量坐标
    lpx, lpy = last_prediction[0], last_prediction[1]  # 上一次预测坐标
    cpx, cpy = current_prediction[0], current_prediction[1]  # 当前预测坐标

    # 绘制从上一次测量到当前测量以及从上一次预测到当前预测的两条线
    cv2.line(frame, (lmx, lmy), (cmx, cmy), (255, 0, 0))  # 蓝色线为测量值
    cv2.line(frame, (lpx, lpy), (cpx, cpy), (0, 0, 255))  # 粉色线为预测值

cv2.namedWindow("kalman_tracker")

# 设置鼠标回调函数
cv2.setMouseCallback("kalman_tracker",mousemove)

while True:
    cv2.imshow("kalman_tracker", frame)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break
cv2.destroyAllWindows()