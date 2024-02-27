from sklearn.cluster import KMeans
import cv2
import numpy as np
import dlib
import matplotlib.pyplot as plt

# 加载dlib的人脸检测器
detector = dlib.get_frontal_face_detector()

# 读取图像
image = cv2.imread('helmet.jpg')

# 使用dlib的人脸检测器检测人脸
dets = detector(image, 1)

def plot_colors(colors):
    # 创建一个空的图像用于显示颜色
    colors_image = np.zeros((50, 300, 3), dtype=np.uint8)
    # 将聚类结果的颜色填充到图像中
    for i in range(len(colors)):
        start_x = int(i * (300 / len(colors)))
        end_x = int((i + 1) * (300 / len(colors)))
        colors_image[:, start_x:end_x, :] = colors[i]
    # 显示颜色图像
    plt.imshow(colors_image)
    plt.axis('off')
    plt.show()

for i, d in enumerate(dets):
    x1 = d.top() if d.top() > 0 else 0
    y1 = d.bottom() if d.bottom() > 0 else 0
    x2 = d.left() if d.left() > 0 else 0
    y2 = d.right() if d.right() > 0 else 0
    face = image[x1:y1, x2:y2]
    # 在图像上画出人脸的边界框
    #cv2.rectangle(image, (x2, x1), (y2, y1), (0, 255, 0), 2)
    # 将人脸图像的颜色空间从BGR转换为RGB
    face_rgb = cv2.cvtColor(face, cv2.COLOR_BGR2RGB)
    # 将人脸图像的形状从(height, width, 3)转换为(height*width, 3)
    face_rgb = face_rgb.reshape((-1, 3))
    # 使用K-means聚类找出人脸中的主要颜色
    kmeans = KMeans(n_clusters=3)
    kmeans.fit(face_rgb)
    # 获取聚类中心，即主要颜色
    colors = kmeans.cluster_centers_
    # 显示聚类结果的颜色
    plot_colors(colors.astype(int))
    # 将主要颜色的颜色空间从RGB转换为YCrCb
    colors_ycrcb = cv2.cvtColor(np.uint8([colors]), cv2.COLOR_RGB2YCrCb)[0]
    # 定义肉色在YCrCb颜色空间中的范围
    lower_skin = np.min(colors_ycrcb, axis=0)
    upper_skin = np.max(colors_ycrcb, axis=0)
    # 将图像的颜色空间从BGR转换为YCrCb
    ycrcb = cv2.cvtColor(image, cv2.COLOR_BGR2YCrCb)
    # 生成肉色的掩膜
    skin_mask = cv2.inRange(ycrcb, lower_skin, upper_skin)
    # 反转肉色掩膜，以过滤掉肉色
    skin_mask = cv2.bitwise_not(skin_mask)
    # 使用肉色掩膜过滤掉图像中的肉色
    result = cv2.bitwise_and(image, image, mask=skin_mask)

# 将图像的颜色空间从BGR转换为HSV
hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

# 定义红色在HSV颜色空间中的范围
lower_red1 = np.array([0, 100, 100], dtype=np.uint8)
upper_red1 = np.array([30, 255, 255], dtype=np.uint8)

lower_red2 = np.array([150, 100, 100], dtype=np.uint8)
upper_red2 = np.array([180, 255, 255], dtype=np.uint8)

# 生成红色的掩膜
red_mask1 = cv2.inRange(hsv, lower_red1, upper_red1)
red_mask2 = cv2.inRange(hsv, lower_red2, upper_red2)

# 合并掩膜
red_mask = cv2.bitwise_or(red_mask1, red_mask2)

# 使用红色掩膜保留图像中的红色
result = cv2.bitwise_and(result, result, mask=red_mask)

#保存图片
cv2.imwrite('test.jpg', result)
# 显示人脸识别的结果
cv2.imshow('Face Detection', image)
# 显示结果
cv2.imshow('image', image)
cv2.imshow('mask', skin_mask)
cv2.imshow('result', result)
cv2.waitKey(0)
cv2.destroyAllWindows()