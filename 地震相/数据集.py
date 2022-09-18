# -*- coding: UTF-8 -*-
"""
@author ：yqy
@Project ：地震相
@Date ：2022/9/17 10:36
"""
import numpy as np
import pandas as pd

data = np.load('C:/workspace/python-workspace/dataSet/seismicFacies/data_train.npz')
label = np.load('C:/workspace/python-workspace/dataSet/seismicFacies/labels_train.npz')

data = data['data']
label = label['labels']

data = data.transpose((2, 1, 0))  # (590, 782, 1006)
label = label.transpose((2, 1, 0))

data = data.transpose((1, 0, 2))  # (782, 590, 1006)
label = label.transpose((1, 0, 2))

nums = len(data)

for i in range(nums):
    pd.DataFrame(data[i]).to_csv('data/%s.csv' % i, header=False, index=False)
    pd.DataFrame(label[i]).to_csv('label/%s.csv' % i, header=False, index=False)
