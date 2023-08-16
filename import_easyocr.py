import easyocr
import os
from PIL import Image
import pytesseract
import sys
import re
import ssl
ssl._create_default_https_context = ssl._create_unverified_context
sys.stdout.reconfigure(encoding='utf-8')

if len(sys.argv) != 2:
     #print("Usage: python import_easyocr.py <image_path>")
     sys.exit(1)

image_path = sys.argv[1]

reader =easyocr.Reader(['ch_tra','en'])
result = reader.readtext(image_path,detail=0)

# 將列表中的字串組合成一個字串
full_string = ''.join(result)
full_string = full_string.replace(" ", "")
print(full_string)

#判斷何種證件
w1 = '保險'
w2 = '學生證'
w3 = '民國'
w4 = '出生'
if full_string.find(w1) != -1:  # 健保卡
    n = 1
elif full_string.find(w2) != -1:
    n = 2
elif full_string.find(w3) != -1 or full_string.find(w4) != -1:
    n = 3
else:
    n = 2

if n==3: 
    # 使用正則表達式找到姓名和統一編號
    name_pattern = r'名(.*?)發'
    name_match = re.search(name_pattern, full_string)
    ##print(name_match)

    if name_match:
        # 提取姓名後面的三個字
        #name = name_match.group(1)[:3]
        chinese_chars = re.findall(r'[\u4e00-\u9fff]', name_match.group(1))
        name = ''.join(chinese_chars)[:3]
        # 提取統一編號的最後 9 位數字
        unified_number = full_string[-9:]
        
        #print(f'姓名後三字：{name} 統一編號後9位：{unified_number}')
    else:
        print("找不到符合的資料")

    # 輸出姓名和統一編號到標準輸出
    print(name)
    print(unified_number)

    result_path = r'C:\Users\USER\Downloads\images\image_0716\result.txt'
    with open(result_path, 'w', encoding='utf-8') as file:
        file.write(f'姓名後三字：{name} 統一編號後9位：{unified_number}\n')
    #print(result)
elif n==2: #學生證
    # 使用正則表達式找到姓名和統一編號
    target_substring = "CARD"
    pattern = re.compile(rf'{re.escape(target_substring)}.*?([\u4e00-\u9fff]+)')
    match = pattern.search(full_string)

    student_id_pattern = r'學號+(\d{7})'  # 匹配"學號"後的七位數字
    name_match = re.search(student_id_pattern, full_string)

    if name_match:
        student_id = name_match.group(1)        
    else:
        print("找不到學號或學號後七位不足。")

    if match:
        first_continuous_chars = match.group(1)
        idnum = first_continuous_chars[:3]
        #print("提取的第一個連續中文字串:", first_continuous_chars)
    else:
        print("找不到符合的連續中文字串。")
    print(idnum)
    print(student_id)
    
elif n==1: #健保卡

    # 使用正則表達式找到"NATIONAL HEALTH"後方的第一個連續中文字串
    target_substring = "HEALTH"

    # 使用正則表達式找到"NATIONAL HEALTH"後方的第一個連續中文字串
    #pattern = re.compile(rf'{re.escape(target_substring)}(.*?)[\u4e00-\u9fff]+')
    #pattern = re.compile(rf'{re.escape(target_substring)}([\u4e00-\u9fff]+)')
    pattern = re.compile(rf'{re.escape(target_substring)}.*?([\u4e00-\u9fff]+)')
    match = pattern.search(full_string)

    if match:
        first_continuous_chars = match.group(1)
        idnum = full_string[match.end() : match.end() + 10]
        #print("提取的第一個連續中文字串:", first_continuous_chars)
    else:
        print("找不到符合的連續中文字串。")
    print(first_continuous_chars)
    print(idnum) 


