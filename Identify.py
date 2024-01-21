import cv2
import numpy as np

def find_luminous_points(image_path, threshold_value=200, min_area=10):
    # 读取图像
    img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

    # 高斯滤波去噪
    img_blur = cv2.GaussianBlur(img, (5, 5), 0)

    # 二值化
    _, img_threshold = cv2.threshold(img_blur, threshold_value, 255, cv2.THRESH_BINARY)

    # 轮廓提取
    contours, _ = cv2.findContours(img_threshold, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # 筛选发光点
    luminous_points = []
    for contour in contours:
        area = cv2.contourArea(contour)
        if area > min_area:
            M = cv2.moments(contour)
            if M["m00"] > 0:
                cX = int(M["m10"] / M["m00"])
                cY = int(M["m01"] / M["m00"])
                luminous_points.append((cX, cY))

    return luminous_points

# 示例用法
image_path = "path/to/your/image.jpg"
luminous_points = find_luminous_points(image_path)

# 打印发光点的坐标
print("Luminous Points:", luminous_points)