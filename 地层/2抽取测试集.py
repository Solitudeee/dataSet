# -*- coding: UTF-8 -*-
"""
@author ：yqy
@Project ：地层
@Date ：2022/10/9 17:48
"""
import numpy as np
import pandas as pd
data=np.load('seismic.npz')
data=data['data']

label=np.load('label.npz')
label=label['data']   #(587, 897, 462)

data = data.transpose((1,0,2))  # (897, 587, 462)
label = label.transpose((1,0,2))

print(data.shape,label.shape)

np.random.seed(344)
indexArr = [i for i in range(0,897)]
indexArr = np.random.choice(indexArr,80,replace=False)

for index in range(80):
    pd.DataFrame(data[indexArr[index],:,:]).to_csv('E:/dataSetHeLan/seismic/%s.csv' % index, header=False, index=False)
    pd.DataFrame(label[indexArr[index],:,:]).to_csv('E:/dataSetHeLan/label/%s.csv' % index, header=False, index=False)

data_train = []
label_train = []
for i in range(897):
    if i not in indexArr:
        data_train.append(data[i,:,:])
        label_train.append(label[i, :, :])


data_train = np.array(data_train)
label_train = np.array(label_train)
print(111,data_train.shape)
print(222,label_train.shape)
np.savez('seismic_train.npz',data=data_train)
np.savez('label_train.npz',data=label_train)
#0-79是测试集