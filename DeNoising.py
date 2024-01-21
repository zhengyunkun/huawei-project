import cv2

def denoise_image(image_path, kernel_size=(5, 5)):
    # 读取图像
    img = cv2.imread(image_path)

    # 高斯滤波去噪
    denoised_img = cv2.GaussianBlur(img, kernel_size, 0)

    return denoised_img

# 示例用法
image_path = "1.jpg"
denoised_image = denoise_image(image_path)

# 保存去噪后的图像到指定目录
cv2.imwrite('1_gray_denoised.jpg', denoised_image)

# 显示原始图像和去噪后的图像
cv2.imshow('Original Image', cv2.imread(image_path))
cv2.imshow('Denoised Image', denoised_image)
cv2.waitKey(0)
cv2.destroyAllWindows()