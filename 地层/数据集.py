# -*- coding: UTF-8 -*-
"""
@author ：yqy
@Project ：地震相
@Date ：2022/9/17 10:36
"""
import numpy as np
import pandas as pd

data = np.load('seismic.npz')
label = np.load('label.npz')

data = data['data']
label = label['data']

print(data.shape)
print(label.shape)

nums = len(data)

for i in range(nums):
    pd.DataFrame(data[i]).to_csv('data/%s.csv' % i, header=False, index=False)
    pd.DataFrame(label[i]).to_csv('label/%s.csv' % i, header=False, index=False)
