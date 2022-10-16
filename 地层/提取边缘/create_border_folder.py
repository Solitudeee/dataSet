# -*- coding: UTF-8 -*-
"""
@author ：yqy
@Project ：论文实验
@Date ：2021/11/13 11:41
"""
import numpy as np
import pandas as pd
from getBorder import getBorder

filePath = "E:/dataSetHeLan/label/"
newFilePath = "E:/dataSetHeLan/border/"


for item in range(4000):
    image = np.array(pd.read_csv(filePath+'%s.csv' % item,header=None))

    print(image.shape)
    border = getBorder(image)
    print(border.shape)

    pd.DataFrame(border).to_csv(newFilePath+'%s.csv' % item, header=False, index=False)