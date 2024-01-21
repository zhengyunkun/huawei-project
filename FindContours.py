import cv2
import numpy as np

def extract_contours(image_path):
    # 读取灰度图像
    gray_img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

    # 使用阈值化分离发光点
    _, thresholded_img = cv2.threshold(gray_img, 200, 255, cv2.THRESH_BINARY)

    # 轮廓提取
    contours, _ = cv2.findContours(thresholded_img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # 创建一个空白图像，绘制轮廓
    contour_img = np.zeros_like(gray_img)
    cv2.drawContours(contour_img, contours, -1, (255), 1)

    return contour_img

# 示例用法
image_path = "1.jpg"
contour_image = extract_contours(image_path)

# 保存去噪后的图像到指定目录
cv2.imwrite('1_contours.jpg', contour_image)

# 显示原始图像和提取的轮廓图像
cv2.imshow('Original Image', cv2.imread(image_path))
cv2.imshow('Contour Image', contour_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
