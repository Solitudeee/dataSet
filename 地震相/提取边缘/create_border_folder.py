# -*- coding: UTF-8 -*-
"""
@author ：yqy
@Project ：论文实验
@Date ：2021/11/13 11:41
"""
import numpy as np
import pandas as pd
from getBorder import getBorder

filePath = "D:\\workspace\\数据集处理\\地震相\\label\\"
newFilePath = "D:\\workspace\\数据集处理\\地震相\\border\\"


for item in range(1000):
    image = np.array(pd.read_csv(filePath+'%s.csv' % item,header=None))

    print(image.shape)
    border = getBorder(image)
    print(border.shape)

    pd.DataFrame(border).to_csv(newFilePath+'%s.csv' % item, header=False, index=False)