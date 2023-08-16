import cv2
import numpy as np

def retain_red_color(image_path):
    try:
        # 開啟圖片
        image = cv2.imread(image_path)

        # 轉換 BGR 色彩空間為 HSV 色彩空間
        hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

        # 定義紅色的 HSV 範圍（OpenCV 中 H 的範圍是 0-179）
        lower_red = np.array([0, 70, 50])
        upper_red = np.array([15, 255, 250])

        # 建立遮罩以保留接近紅色的部分
        mask = cv2.inRange(hsv_image, lower_red, upper_red)

        # 將接近紅色的部分填充為白色，其餘部分填充為黑色
        result_image = np.zeros_like(image)
        result_image[mask > 0] = [255, 255, 255]

        return result_image
    except Exception as e:
        print(f"處理圖片出現錯誤：{e}")
        return None

# 假設你的上傳圖片的路徑是 input_image.jpg
input_path = r"C:\Users\USER\Downloads\images\image_0709\test.jpg"

# 保留接近紅色的部分並儲存
result_image = retain_red_color(input_path)

if result_image is not None:
    # 儲存處理後的圖片
    output_path = r"C:\Users\USER\Downloads\images\image_0709\my_result.jpg"
    cv2.imwrite(output_path, result_image)
    print("圖片處理完成，已儲存為 result_image.jpg")