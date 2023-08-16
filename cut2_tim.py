import cv2
import matplotlib.pyplot as plt
import matplotlib.image as img

#失敗的身分證裁切
def find_id_card_region(image_path):
    try:
        # 開啟圖片
        image = cv2.imread(image_path)

        # 將圖片轉換成灰度圖像
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        # 使用 Canny 邊緣檢測找出輪廓
        edges = cv2.Canny(gray, 30, 150)
        print(edges)

        # 找出輪廓
        contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        # 假設身分證為最大輪廓
        max_contour = max(contours, key=cv2.contourArea)

        # 獲取最大輪廓的邊界框
        x, y, w, h = cv2.boundingRect(max_contour)

        return x, y, w, h
    except Exception as e:
        print(f"出現錯誤：{e}")
        return None

def crop_to_id_card(image_path, output_path):
    try:
        # 辨識身分證位置
        x, y, w, h = find_id_card_region(image_path)
        #x,y是起始點座標 w,h是寬高
        print(x,y,w,h)

        img = cv2.imread(image_path)
        red_color = (0,0,255)
        cv2.rectangle(img,(x,y),(w,h),red_color,3,cv2.LINE_AA)
        plt.imshow(img)
        plt.show()

        # 調整裁切範圍，增加一點寬度和高度，以保證滿版身分證在圖片中
        x -= 10
        y -= 10
        

        x1 = x
        y1 = y 
        

        # 限制裁切範圍不超出原始圖片大小
        image = cv2.imread(image_path)
        h, w, _ = image.shape
        x = max(0, x)
        y = max(0, y)
        w = min(w - x, w)
        h = min(h - y, h)
        
        h1, w1, _ = image.shape
        w1 -= 100
        h1 -= 200
        x1 = max(0, x)
        y1 = max(0, y)
        w1 = min(w1 - x1-10, w1-10)
        h1 = min(h1 - y1-10, h1-10)


        # 開啟圖片
        image = cv2.imread(image_path)

        # 裁剪圖片
        cropped_image = image[y:y+h, x:x+w]
        cropped_image2 = image[y1:y1+h1, x1:x1+w1]

        # 儲存裁剪後的圖片
        cv2.imwrite(output_path, cropped_image)
        cv2.imwrite(r"C:\Users\USER\Downloads\images\image_0709\output2_image2.jpg", cropped_image2)

        plt.imshow(cropped_image)
        plt.show()
        plt.imshow(cropped_image2)
        plt.show()

        print("身分證辨識並裁剪完成")
    except Exception as e:
        print(f"出現錯誤：{e}")

# 假設你的上傳圖片的路徑是 input_image.jpg，並且想要將裁切後的圖片儲存為 output_image.jpg
input_path = r"C:\Users\USER\Downloads\images\image_0709\B975EAAF-8FEC-4D4F-A5F1-2867D8809515.jpg"
output_path = r"C:\Users\USER\Downloads\images\image_0709\S__24436794_output_image.jpg"

# 輸入圖片路徑和儲存路徑，執行裁切
crop_to_id_card(input_path, output_path)
