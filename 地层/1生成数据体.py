# -*- coding: UTF-8 -*-
"""
@author ：yqy
@Project ：地层
@Date ：2022/10/8 22:05
"""
import numpy as np
import pandas as pd

data = []

for i in range(104,691):
    path = "C:/workspace/python-workspace/helanData/data/seismic/iline="+str(i)+".bin"
    profile = np.fromfile(path, dtype=np.float32)
    profile.shape = (897, 462)
    data.append(profile)
data = np.array(data)   #(587, 897, 462)
print(data.shape)
np.savez('seismic.npz',data=data)

label = []
for i in range(104,691):
    path = "C:/workspace/python-workspace/helanData/data/facies/iline="+str(i)+".bin"
    profile = np.fromfile(path, dtype=np.float32)
    profile.shape = (897, 462)
    label.append(profile)
label = np.array(label)   #(587, 897, 462)
print(label.shape)
np.savez('label.npz',data=label)