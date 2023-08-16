import os
from PIL import Image
import pytesseract
import sys

def convert_image_format(input_path, output_path, output_format='JPEG'):
    image = Image.open(input_path)
    image.save(output_path, format=output_format)

def main():
    # 轉換圖片格式
    #input_image_path = 'D:\\xampp\\htdocs\\test_data.heic'  # 輸入的 .heic 相片路徑
    #output_image_path = 'D:\\xampp\\htdocs\\test_data.jpg'  # 轉換後的 .jpg 圖片儲存路徑
    #convert_image_format(input_image_path, output_image_path, output_format='JPEG')
    
    #input_image_path = r'C:\Users\USER\Downloads\IMG_3835.HEIC'  # 輸入的 .heic 相片路徑
    output_image_path =r"C:\Users\USER\Downloads\灰階1.jpg"  # 轉換後的 .jpg 圖片儲存路徑
    #214身分證 213健保卡 211相片學生證 224掃描學生證
    #output_image_path2 =r'C:\Users\USER\Downloads\name\S__24158212.jpg'
    #output_image_path3 =r'C:\Users\USER\Downloads\name\S__24158212.jpg'
    #convert_image_format(input_image_path, output_image_path, output_format='JPEG')

    pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

    img = Image.open(output_image_path) #我測試


    text = pytesseract.image_to_string(img, config="--psm 4", lang='chi_tra+num') #繁體中文
    with open('D:\\xampp\\htdocs\\result.txt', 'w') as file:
        file.write(str(text))
    #text="hello"
    print(text)

if __name__ == '__main__':
    main()