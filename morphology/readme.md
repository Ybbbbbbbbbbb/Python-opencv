###     形态学处理

- 形态学两个基本运算是---- 膨胀与腐蚀

- 膨胀与腐蚀有以下作用：
  - 消除噪声
  - 分割出独立的图像元素，在图像中连接相邻的元素
  - 寻找图像中明显的极大值区域或者极小值区域
  - 求图像的梯度

- 从数学角度来讲，膨胀和腐蚀就是将图像与核进行卷积，核可以是任意形状和大小

- 膨胀（dilate) 卷积核与图像卷积，计算核覆盖区域像素点的最大值，并把这个最大值赋给参考点指定的像素。

- 腐蚀（erode）求局部最小值，计算核覆盖区域的像素点的最小值，把这个最小值赋给参考点指定的像素

- 开运算 实际上是 先腐蚀 在膨胀


$$
  dist = open(src,element) = dilate(erode(src, element))
$$

- 闭运算 实际上是想膨胀在腐蚀


$$
dist = close(src, element) = erode(dilate(src, element))
$$

- 形态学梯度 膨胀图于腐蚀图之差


$$
  dist = morph-gradd(src, element) = dilate(src, element) - erode(src, element)
$$



- 顶帽（top hat） 原图与开运算图之差 


$$
  dist = tophat(src, element) = src - open(src, elemnt)
$$



- 黑帽（black hat）原图与闭运算图之差



  dist = blackhat(src, element) = src - close(src, element)

（以上内容参考   https://blog.csdn.net/yangleo1987/article/details/53168423      )