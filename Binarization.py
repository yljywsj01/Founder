import cv2
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as img
import os

img = cv2.imread(r"C:\Users\USER\Downloads\images\image_0716\B975EAAF-8FEC-4D4F-A5F1-2867D8809515.jpg")

print("圖呢")
# get grayscale image
def get_grayscale(image):
    return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# noise removal
def remove_noise(image):
    # image=cv2.GaussianBlur(image, (13,13),0)
    # return cv2.medianBlur(image,5)
    image2=cv2.medianBlur(image,5)
    return cv2.GaussianBlur(image2, (7,7),0)

# thresholding
def thresholding(image):
    return cv2.threshold(image, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]
#def thresholding(image):
#    return cv2.threshold(image, 0, 255, cv2.THRESH_BINARY)[1]


# dilation
def dilate(image):
    kernel = np.ones((5, 5), np.uint8)
    return cv2.dilate(image, kernel, iterations=1)

# erosion
def erode(image):
    kernel = np.ones((5, 5), np.uint8)
    return cv2.erode(image, kernel, iterations=1)

# opening - erosion followed by dilation
def opening(image):
    kernel = np.ones((5, 5), np.uint8)
    return cv2.morphologyEx(image, cv2.MORPH_OPEN, kernel)

# canny edge detection
def canny(image):
    return cv2.Canny(image, 100, 200)

# skew correction
def deskew(image):
    coords = np.column_stack(np.where(image > 0))
    angle = cv2.minAreaRect(coords)[-1]
    if angle < -45:
        angle = -(90 + angle)
    else:
        angle = -angle
    (h, w) = image.shape[:2]
    center = (w // 2, h // 2)
    M = cv2.getRotationMatrix2D(center, angle, 1.0)
    rotated = cv2.warpAffine(image, M, (w, h), flags=cv2.INTER_CUBIC, borderMode=cv2.BORDER_REPLICATE)
    return rotated

# template matching
def match_template(image, template):
    return cv2.matchTemplate(image, template, cv2.TM_CCOEFF_NORMED)

#plt.imshow(img)
#plt.show()

# 儲存處理過的圖片

gray = get_grayscale(img)
cv2.imwrite(r"C:\Users\USER\Downloads\images\image_0716\1539_gray.jpg", gray)
#plt.subplot(221)
#plt.imshow(gray)                                    # 在圖表中繪製圖片

print("幹")
noise_removed = remove_noise(gray)
cv2.imwrite(r"C:\Users\USER\Downloads\images\image_0716\1020_noise_removed.jpg", noise_removed)
#plt.subplot(222)
#plt.imshow(noise_removed)                                    # 在圖表中繪製圖片

thresholded = thresholding(noise_removed)
cv2.imwrite(r"C:\Users\USER\Downloads\images\image_0716\jenny.jpg", thresholded)
#plt.subplot(223)
#plt.imshow(thresholded)                                    # 在圖表中繪製圖片

#dilated = dilate(thresholded)
#cv2.imwrite(r"C:\Users\USER\Downloads\name\S__24158224_dilated.jpg", dilated)
#plt.subplot(224)
#plt.imshow(dilated)

#plt.show()

eroded = erode(thresholded)
cv2.imwrite(r"C:\Users\USER\Downloads\name\S__24158224_eroded.jpg", eroded)

opened = opening(thresholded)
cv2.imwrite(r"C:\Users\USER\Downloads\name\S__24158224_opened.jpg", opened)

edges = canny(gray)
cv2.imwrite(r"C:\Users\USER\Downloads\name\S__24158224_edges.jpg", edges)

rotated = deskew(gray)
cv2.imwrite(r"C:\Users\USER\Downloads\name\S__24158224_rotated.jpg", rotated)

template = cv2.imread(r"C:\Users\USER\Downloads\name_S__24158224.jpg", 0)
result = match_template(gray, template)
cv2.imwrite(r"C:\Users\USER\Downloads\name\S__24158224_template_matching.jpg", result)
