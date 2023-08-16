
#他口
#"C:\Users\USER\Downloads\images\image_0709\S__24436794.jpg"  
#我
#"C:\Users\USER\Downloads\images\image_0709\B975EAAF-8FEC-4D4F-A5F1-2867D8809515.jpg"
import cv2
from PIL import Image
import matplotlib.pyplot as plt
import matplotlib.image as img
import numpy as np
import os

def adjust_image_color(image_path):
    try:
        # 開啟圖片
        image = cv2.imread(image_path)

        # 色彩均衡處理
        r, g, b = cv2.split(image)

        # 對每個通道進行色彩均衡處理
        r = cv2.equalizeHist(r)
        g = cv2.equalizeHist(g)
        b = cv2.equalizeHist(b)

        # 將處理後的通道合併回圖片
        equalized_image = cv2.merge([r, g, b])

        return equalized_image
    except Exception as e:
        print(f"調整顏色出現錯誤：{e}")
        return None
    
def crop_and_resize_image(input_path, output_path, target_width, target_height):
    try:
        # 開啟圖片
        image = Image.open(input_path)

        # 調整尺寸
        resized_image = image.resize((target_width, target_height))

        # 儲存調整後的圖片
        resized_image.save(output_path)

        print("圖片裁剪並調整尺寸完成")
    except Exception as e:
        print(f"裁切出現錯誤：{e}")

img = cv2.imread(r"C:\Users\USER\Downloads\image_0716\005.jpg")

# get grayscale image
def get_grayscale(image):
    return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# noise removal
def remove_noise(image):
    #image2=cv2.GaussianBlur(image, (13,13),0)
    #return cv2.medianBlur(image,5)
    image2=cv2.medianBlur(image,5)
    return cv2.GaussianBlur(image2, (7,7),0)

# thresholding
def thresholding(image):
    return cv2.threshold(image, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]
#def thresholding(image):
#    return cv2.threshold(image, 0, 255, cv2.THRESH_BINARY)[1]

# 假設你的上傳圖片的路徑是 input_image.jpg

#他口
#input_path = r"C:\Users\USER\Downloads\images\image_0709\S__24436794.jpg"
#output_path = r"C:\Users\USER\Downloads\images\image_0709\S__24436794_output_image.jpg"

#我
input_path = r"C:\Users\USER\Downloads\images\image_0709\B975EAAF-8FEC-4D4F-A5F1-2867D8809515.jpg"
output_path = r"C:\Users\USER\Downloads\images\image_0709\new_smallsize.jpg"

target_width = 1120
target_height = 700

# 1. 調整該圖片的色彩分布
processed_image = adjust_image_color(input_path)

if processed_image is not None:
    # 儲存調整後的圖片
    cv2.imwrite(output_path, processed_image)
    cv2.imwrite(r"C:\Users\USER\Downloads\images\image_0709\test.jpg", processed_image)
    print("照片處理完成")

# 2. 執行圖片裁剪及尺寸調整
crop_and_resize_image(output_path, output_path, target_width, target_height)

# 3. 二質化處理
img = cv2.imread(output_path)
gray = get_grayscale(img)
cv2.imwrite(output_path, gray)
plt.subplot(221)
plt.imshow(gray)                                    # 在圖表中繪製圖片

processed_image = adjust_image_color()
if processed_image is not None:
    # 儲存調整後的圖片
    cv2.imwrite(output_path, processed_image)
    cv2.imwrite(r"C:\Users\USER\Downloads\images\image_0709\test1.jpg", processed_image)
    print("照片處理完成2")

noise_removed = remove_noise(processed_image)
cv2.imwrite(output_path, noise_removed)
plt.subplot(222)
plt.imshow(noise_removed)                                # 在圖表中繪製圖片

thresholded = thresholding(noise_removed)
print("快沒了")
cv2.imwrite(output_path, thresholded)
plt.subplot(223)
plt.imshow(thresholded)    
print("二質化完成")

plt.show()
