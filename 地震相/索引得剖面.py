# -*- coding: UTF-8 -*-
"""
@author ：yqy
@Project ：地震相
@Date ：2022/9/17 14:02
"""
#由剖面索引文件得到剖面

import numpy as np
from main import MainWindow
import sys
from PyQt5 import  QtWidgets
import linecache
import pandas as pd

#读取数据体，并展开成平面
data = np.load('C:/workspace/python-workspace/dataSet/seismicFacies/data_train.npz')
label = np.load('C:/workspace/python-workspace/dataSet/seismicFacies/labels_train.npz')

data = data['data']
label = label['labels']

data = data.transpose((2, 1, 0))  # (590, 782, 1006)
label = label.transpose((2, 1, 0))

newData = []
newLabel = []


for i in range(590):
    newData.extend(data[i])
    newLabel.extend(label[i])

newData = np.array(newData)
newLabel = np.array(newLabel)

print(newData.shape)
print(newLabel.shape)

np.random.seed(222)
indexArr = [i for i in range(1,116218)]
indexArr = np.random.choice(indexArr,116218)

# path = np.array(linecache.getline("profile.txt",116037).strip("[").strip("]\n").split(','))#读索引
# print(path)

count = 0
#逐行读取索引文件，并保存剖面
for index in indexArr:
    print(count,'----116218',index)
    path = np.array(linecache.getline("profile.txt",index).strip("[").strip("]\n").split(','))#读索引
    path = [int(i) for i in path]
    # print(len(path))
    profile = newData[path, :]    #得剖面
    label = newLabel[path, :]     #得标签
    pd.DataFrame(profile).to_csv('seismic/%s.csv' % count, header=False, index=False)
    pd.DataFrame(label).to_csv('label/%s.csv' % count, header=False, index=False)
    count = count + 1
    # app = QtWidgets.QApplication(sys.argv)
    # mainWindow = MainWindow(label)
    # mainWindow.show()
    # sys.exit(app.exec_())



#逐行读取索引文件，并保存剖面
# with open("profile.txt", 'r') as f:
#     for index in indexArr:
#         path = np.array(f.readline().strip("[").strip("]\n").split(','))  #读索引
#         path = [int(i) for i in path]
#         # print(path.shape)
#         profile = newData[path, :]    #得剖面
#         label = newLabel[path, :]     #得标签

        # app = QtWidgets.QApplication(sys.argv)
        # mainWindow = MainWindow(label)
        # mainWindow.show()
        # sys.exit(app.exec_())





