import numpy as np
import pandas as pd

data = np.load('data.npz')
label = np.load('label.npz')

data = data['data']
label = label['data']


newData = []
newLabel = []


for i in range(587):
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
