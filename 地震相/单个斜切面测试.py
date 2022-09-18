import numpy as np
import pandas as pd

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

way = []
x = 0
for i in range(590):
    way.append(x)
    x = x + 783
print(way)
profile = newLabel[way,:]
print(profile.shape)

from main import MainWindow
import sys
from PyQt5 import  QtWidgets
app = QtWidgets.QApplication(sys.argv)
mainWindow = MainWindow(profile)
mainWindow.show()
sys.exit(app.exec_())
