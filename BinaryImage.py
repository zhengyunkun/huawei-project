import cv2

def threshold_image(image_path, threshold_value=200):
    # 读取灰度图像
    gray_img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

    # 使用阈值化分离发光点
    _, thresholded_img = cv2.threshold(gray_img, threshold_value, 255, cv2.THRESH_BINARY)

    return thresholded_img

# 示例用法
image_path = "1_gray.jpg"
thresholded_image = threshold_image(image_path)

# 保存二值图像到指定目录
cv2.imwrite('1_gray_threshold.jpg', thresholded_image)

# 显示原始图像和阈值化后的图像
cv2.imshow('Original Image', cv2.imread(image_path))
cv2.imshow('Thresholded Image', thresholded_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
