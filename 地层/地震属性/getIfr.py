# -*- coding: UTF-8 -*-
"""
@author ：yqy
@Project ：多属性实验   瞬时属性
@Date ：2021/11/30 8:34
"""
import numpy as np
from scipy.fftpack import hilbert
import pandas as pd

filePath = "E:/dataSetHeLan/seismic/"
newFilePath = "E:/dataSetHeLan/ifr/"

freq = 1/462
for item in range(4000):
    image = np.array(pd.read_csv(filePath+'%s.csv' % item,header=None))
    print(image.shape)  #(782, 1006)
    image = image.T  #(1006, 782)
    res = []
    for i in range(587):
        st = image[:, i]
        hilbert_f = hilbert(st)
        pha = np.arctan(hilbert_f / st)
        ifr = list((pha[1:] - pha[:-1]) / freq)
        ifr.insert(0, ifr[0])
        ifr = np.array(ifr)
        res.append(ifr)

    res = np.array(res,dtype=np.float32)
    print(res.shape)
    pd.DataFrame(res).to_csv(newFilePath+'%s.csv' % item, header=False, index=False)






