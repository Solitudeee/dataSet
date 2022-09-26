# -*- coding: UTF-8 -*-
"""
@author ：yqy
@Project ：多属性实验   瞬时属性
@Date ：2021/11/30 8:34
"""
import numpy as np
from scipy.fftpack import hilbert
import pandas as pd

filePath = "D:\\workspace\\数据集处理\\地震相\\seismic\\"
newFilePath = "D:\\workspace\\数据集处理\\地震相\\pha\\"

for item in range(1000,4000):
    image = np.array(pd.read_csv(filePath+'%s.csv' % item,header=None))
    print(image.shape)  #(782, 1006)
    image = image.T  #(1006, 782)
    res = []
    for i in range(590):
        print(item,"----------",i)
        st = image[:, i]
        hilbert_f = hilbert(st)
        res.append(np.arctan(hilbert_f / st))

    res = np.array(res,dtype=np.float32)
    print(res.shape)
    pd.DataFrame(res).to_csv(newFilePath+'%s.csv' % item, header=False, index=False)






