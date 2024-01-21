import cv2

def convert_to_grayscale(image_path):
    # 读取彩色图像
    img = cv2.imread(image_path)

    # 转换为灰度图像
    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # 保存灰度图像到指定目录
    output_path = "1_gray.jpg"
    cv2.imwrite(output_path, gray_img)

    return gray_img

# 示例用法
image_path = "1.jpg"
gray_image = convert_to_grayscale(image_path)

# 显示原始图像和灰度图像
cv2.imshow('Original Image', cv2.imread(image_path))
cv2.imshow('Grayscale Image', gray_image)

cv2.waitKey(0)
cv2.destroyAllWindows()