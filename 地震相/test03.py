# -*- coding: UTF-8 -*-
"""
@author ：yqy
@Project ：地震相
@Date ：2022/9/17 15:44
"""
import linecache

text = linecache.getline("profile.txt",461370)
print(text)

with open("profile.txt", 'r') as f:
    for i in range(461380):
        print(i,len(f.readline()))