import math
import pytesseract
import cv2
from PIL import Image

# 轉換圖像為白底黑字，提高識別准確性
def transformedImage():

    # 計算兩個顏色之間的歐幾里得距離
    def color_distance(c1, c2):
        r1, g1, b1 = c1
        r2, g2, b2 = c2
        return math.sqrt((r1 - r2) ** 2 + (g1 - g2) ** 2 + (b1 - b2) ** 2)

    # 打開原圖
    img = Image.open(r"C:\Users\USER\Downloads\7A675EDB-F3F5-496F-BFBA-1173FE5BECC6.jpg")
    # 創建一個白色的背景圖像
    bg_img = Image.new('RGB', img.size, (255, 255, 255))
    # 定義相似顏色的閾值
    threshold = 100

    # 遍歷所有像素點
    for x in range(img.width):
        for y in range(img.height):
            # 獲取當前像素點的顏色
            color = img.getpixel((x, y))
            # 如果原圖當前坐標顏色與給定顏色相似，則在背景圖中相同的坐標寫入黑色像素點
            if color_distance(color, (247, 245, 244)) < threshold:
                bg_img.putpixel((x, y), (0, 0, 0))

    # 保存新圖像
    bg_img.save(r"C:\Users\USER\Downloads\7A675EDB-F3F5-496F-BFBA-1173FE5BECC6_new.jpg")

    applyThreshold()

# 應用色階和二值化
def applyThreshold():
    img = cv2.imread(r"C:\Users\USER\Downloads\7A675EDB-F3F5-496F-BFBA-1173FE5BECC6_new.jpg")  # 讀取新圖像
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  # 轉換為灰度圖像
    _, threshold_img = cv2.threshold(img_gray, 111, 113, cv2.THRESH_BINARY)  # 進行二值化處理
    cv2.imwrite(r"C:\Users\USER\Downloads\7A675EDB-F3F5-496F-BFBA-1173FE5BECC6_new.jpg", threshold_img)  # 保存二值化圖片

    characterRecognition()

# 文字識別
def characterRecognition():
    img = cv2.imread(r"C:\Users\USER\Downloads\7A675EDB-F3F5-496F-BFBA-1173FE5BECC6.jpg")  # 讀取二值化圖像
    config = "--psm 7 --oem 3 -c tessedit_char_whitelist=0123456789"  # 設定文字識別的參數
    text = pytesseract.image_to_string(img, config=config)  # 進行文字識別
    try:
        text = int(''.join(filter(str.isdigit, text)))  # 去除其他符號，將識別的數字進行重新整合
    except Exception:
        text = 1

if __name__ == "__main__":
    transformedImage()
