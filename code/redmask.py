import cv2
import numpy as np
import dlib
image = cv2.imread('helmet.jpg')
# 将图像从BGR颜色空间转换为HSV颜色空间
hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
# 定义红色的HSV颜色范围
lower_red1 = np.array([0,50,50])
upper_red1 = np.array([10,255,255])
lower_red2 = np.array([170,50,50])
upper_red2 = np.array([180,255,255])

# 生成掩膜
mask1 = cv2.inRange(hsv, lower_red1, upper_red1)
mask2 = cv2.inRange(hsv, lower_red2, upper_red2)
mask = cv2.bitwise_or(mask1, mask2)
# 使用掩膜过滤掉图像中的人脸
result = cv2.bitwise_and(image, image, mask=mask)
cv2.imwrite('first.jpg',result)