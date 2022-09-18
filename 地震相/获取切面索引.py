# -*- coding: UTF-8 -*-
"""
@author ：yqy
@Project ：地震相
@Date ：2022/9/17 14:59
"""
#取所有点

rightBorder = []
for i in range(1,591):
    rightBorder.append(i*782)


print(rightBorder)

profile = []
count = 0

with open("profile.txt", 'w') as f:

    for index in range(782*590):
        print(index,"-----",782*590)

        #右上
        path = []
        x = index
        for i in range(590):
            path.append(x)
            x = x-781
            if x < 0:
                break
        if len(path) == 590:
            count = count+1
            # profile.append(path)
            f.writelines(str(path))
            f.writelines("\n")

        # 右
        path = []
        x = index
        for i in range(590):
            path.append(x)
            x = x + 1
            if x in rightBorder:
                break
        if len(path) == 590:
            count = count + 1
            # profile.append(path)
            f.writelines(str(path))
            f.writelines("\n")


        # 右下
        path = []
        x = index
        for i in range(590):
            path.append(x)
            x = x + 783
            if x > 590*782:
                break
        if len(path) == 590:
            count = count + 1
            # profile.append(path)
            f.writelines(str(path))
            f.writelines("\n")

        # 下
        path = []
        x = index
        for i in range(590):
            path.append(x)
            x = x + 782
            if x > 590*782:
                break
        if len(path) == 590:
            count = count + 1
            # profile.append(path)
            f.writelines(str(path))
            f.writelines("\n")

print("count:",count)