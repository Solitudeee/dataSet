# -*- coding: utf-8 -*-
"""
Created on Thu Dec  7 21:12:41 2017

@author: L.P.S
"""

import matplotlib.pyplot as plt
import numpy as np
import math

def getBorder(input):
    sigma1 = sigma2 = 1
    sum = 0

    gaussian = np.zeros([5, 5])
    for i in range(5):
        for j in range(5):
            gaussian[i, j] = math.exp(-1 / 2 * (np.square(i - 3) / np.square(sigma1)  # 生成二维高斯分布矩阵
                                                + (np.square(j - 3) / np.square(sigma2)))) / (2 * math.pi * sigma1 * sigma2)
            sum = sum + gaussian[i, j]

    gaussian = gaussian / sum


    # step1.高斯滤波
    W, H = input.shape
    new_gray = np.zeros([W - 5, H - 5])
    for i in range(W - 5):
        for j in range(H - 5):
            new_gray[i, j] = np.sum(input[i:i + 5, j:j + 5] * gaussian)  # 与高斯矩阵卷积实现滤波

    # plt.imshow(new_gray, cmap="gray")

    # new_gray= input

    # step2.增强 通过求梯度幅值
    W1, H1 = new_gray.shape
    dx = np.zeros([W1 - 1, H1 - 1])
    dy = np.zeros([W1 - 1, H1 - 1])
    d = np.zeros([W1 - 1, H1 - 1])
    for i in range(W1 - 1):
        for j in range(H1 - 1):
            dx[i, j] = new_gray[i, j + 1] - new_gray[i, j]
            dy[i, j] = new_gray[i + 1, j] - new_gray[i, j]
            d[i, j] = np.sqrt(np.square(dx[i, j]) + np.square(dy[i, j]))  # 图像梯度幅值作为图像强度值

    NMS = np.copy(d)
    # NMS = new_gray


    # step4. 双阈值算法检测、连接边缘
    W3, H3 = NMS.shape
    DT = np.zeros([W3, H3])
    # 定义高低阈值
    TL = 0.1 * np.max(NMS)
    TH = 0.3 * np.max(NMS)
    print(TL, TH)
    for i in range(1, W3 - 1):
        for j in range(1, H3 - 1):
            if (NMS[i, j] < TL):
                DT[i, j] = 0
            elif (NMS[i, j] > TH):
                DT[i, j] = 1
            elif ((NMS[i - 1, j - 1:j + 1] < TH).any() or (NMS[i + 1, j - 1:j + 1]).any()
                  or (NMS[i, [j - 1, j + 1]] < TH).any()):
                DT[i, j] = 1

    plt.imshow(DT, cmap="gray")
    return DT


if __name__ == '__main__':
    import sys
    import pandas as pd
    from main import MainWindow
    from PyQt5 import QtWidgets
    from dilate import dilate_bin_image


    filePath = "D:\\workspace\\数据集处理\\地震相\\label\\"
    item = 0
    input = np.array(pd.read_csv(filePath + '%s.csv' % item, header=None))
    input = getBorder(input)

    # kernel = np.ones(shape=(5, 5))  #无,3,5,7,9
    # input = dilate_bin_image(input, kernel)

    # pd.DataFrame(getBorder(input)).to_csv('%s.csv' % item, header=False, index=False)

    app = QtWidgets.QApplication(sys.argv)
    mainWindow = MainWindow(input)
    mainWindow.show()
    sys.exit(app.exec_())
