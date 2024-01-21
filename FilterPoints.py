import cv2
import numpy as np

def filter_luminous_points(image_path, threshold_value=200, min_area=10):
    # 读取灰度图像
    gray_img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

    # 使用阈值化分离发光点
    _, thresholded_img = cv2.threshold(gray_img, threshold_value, 255, cv2.THRESH_BINARY)

    # 轮廓提取
    contours, _ = cv2.findContours(thresholded_img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

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

    # 在原始图像上绘制筛选后的发光点
    result_img = cv2.imread(image_path)
    for point in luminous_points:
        cv2.circle(result_img, point, 5, (0, 255, 0), -1)

    return result_img

# 示例用法
image_path = "1.jpg"
result_image = filter_luminous_points(image_path)

# 保存筛选后的图像到指定目录
cv2.imwrite('1_result.jpg', result_image)

# 显示原始图像和筛选后的图像
cv2.imshow('Original Image', cv2.imread(image_path))
cv2.imshow('Result Image', result_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
