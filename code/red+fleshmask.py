import cv2
import numpy as np
import dlib

# 加载dlib的人脸检测器
detector = dlib.get_frontal_face_detector()

# 读取图像
image = cv2.imread('helmet.jpg')

# 使用dlib的人脸检测器检测人脸
dets = detector(image, 1)

# 将图像从BGR颜色空间转换为YCrCb颜色空间
ycrcb = cv2.cvtColor(image, cv2.COLOR_BGR2YCrCb)

for i, d in enumerate(dets):
    x1 = d.top() if d.top() > 0 else 0
    y1 = d.bottom() if d.bottom() > 0 else 0
    x2 = d.left() if d.left() > 0 else 0
    y2 = d.right() if d.right() > 0 else 0
    face_ycrcb = ycrcb[x1:y1, x2:y2]

    # 定义肉色在YCrCb颜色空间中的范围
    lower_skin = np.array([0, 133, 77], dtype=np.uint8)
    upper_skin = np.array([255, 173, 127], dtype=np.uint8)

    # 生成肉色的掩膜
    skin_mask = cv2.inRange(face_ycrcb, lower_skin, upper_skin)

    # 将肉色掩膜的尺寸扩展到和图像相同
    skin_mask = cv2.resize(skin_mask, (image.shape[1], image.shape[0]))

    # 定义红色在BGR颜色空间中的范围
    lower_red = np.array([0, 0, 100], dtype=np.uint8)
    upper_red = np.array([50, 50, 255], dtype=np.uint8)

    # 生成红色的掩膜
    red_mask = cv2.inRange(image, lower_red, upper_red)

    # 使用肉色掩膜过滤掉图像中的肉色
    result = cv2.bitwise_and(image, image, mask=skin_mask)

    # 使用红色掩膜保留图像中的红色
    result = cv2.bitwise_and(result, result, mask=red_mask)

    cv2.imwrite('color.jpg',result)

    # 显示结果
    cv2.imshow('image', image)
    cv2.imshow('mask', skin_mask)
    cv2.imshow('result', result)
    cv2.waitKey(0)
    cv2.destroyAllWindows()