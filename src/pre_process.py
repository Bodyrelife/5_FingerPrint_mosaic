# coding=UTF-8
import os
import cv2
import numpy as np

database = '..\database'
debug = 1

def equalize_hist(image):
    hist, bins = np.histogram(image.flatten(), 256, [0, 256])
    cdf = hist.cumsum()  # 计算累积直方图
    cdf_m = np.ma.masked_equal(cdf, 0)  # 除去直方图中的0值
    cdf_m = (cdf_m - cdf_m.min()) * 255 / (cdf_m.max() - cdf_m.min())  # 等同于前面介绍的lut[i] = int(255.0 *p[i])公式
    cdf = np.ma.filled(cdf_m, 0).astype('uint8')  # 将掩模处理掉的元素补为0
    return cv2.LUT(image, cdf)


def pre_process_debug(image):
    cv2.imshow("Image", image)
    image_eqhist = equalize_hist(image)
    cv2.imshow("Equalize Hist", image_eqhist)
    image_blur = cv2.medianBlur(image, 5)
    cv2.imshow("Blur", image_blur)
    image_blur_eqhist = equalize_hist(image_blur)
    cv2.imshow("Blur + Equalize Hist", image_blur_eqhist)
    image_eqhist_blur = cv2.medianBlur(image_eqhist, 5)
    cv2.imshow("Equalize Hist + Blur", image_eqhist_blur)
    cv2.waitKey(0)


def load_image(pic_folder):
    pics = os.listdir(os.path.join(database, pic_folder))
    for pic in pics:
        if os.path.splitext(pic)[1] == '.bmp':
            img = cv2.imread(os.path.join(database, pic_folder, pic))
            pre_process(img)


def main():
    pic_folders = os.listdir(database)
    for pic_folder in pic_folders:
        load_image(pic_folder)
    cv2.destroyAllWindows()


if __name__ == '__main__':
    main()




