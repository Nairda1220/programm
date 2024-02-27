import cv2
import numpy as np
import dlib

# 加载dlib的人脸检测器
detector = dlib.get_frontal_face_detector()

# 读取图像
image = cv2.imread('helmet.jpg')

# 使用dlib的人脸检测器检测人脸
dets = detector(image, 1)

# 创建一个新的全白掩膜
face_mask = np.ones(image.shape[:2], dtype="uint8") * 255  # 修改这一行

# 对于检测到的每一个人脸，将掩膜中对应的部分设为黑色
for i, d in enumerate(dets):
    x1 = d.top() if d.top() > 0 else 0
    y1 = d.bottom() if d.bottom() > 0 else 0
    x2 = d.left() if d.left() > 0 else 0
    y2 = d.right() if d.right() > 0 else 0
    face_mask[x1:y1, x2:y2] = 0

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

# 将人脸掩膜应用到红色掩膜上
mask = cv2.bitwise_and(mask, face_mask)

# 使用掩膜过滤掉图像中的人脸
result = cv2.bitwise_and(image, image, mask=mask)

cv2.imwrite('image.jpg',result)

# 显示结果
cv2.imshow('image', image)
cv2.imshow('mask', mask)
cv2.imshow('result', result)
cv2.waitKey(0)
cv2.destroyAllWindows()