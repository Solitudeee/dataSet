# -*- coding: UTF-8 -*-
"""
@author ：yqy
@Project ：地震相
@Date ：2022/9/17 14:59
"""
#取所有点

rightBorder = []
for i in range(1,588):
    rightBorder.append(i*817)


print(rightBorder)

profile = []
count = 0

with open("profile.txt", 'w') as f:

    for index in range(817*587):
        print(index,"-----",782*590)

        #右上
        path = []
        x = index
        for i in range(587):
            path.append(x)
            x = x-816
            if x < 0:
                break
        if len(path) == 587:
            count = count+1
            # profile.append(path)
            f.writelines(str(path))
            f.writelines("\n")

        # 右
        path = []
        x = index
        for i in range(587):
            path.append(x)
            x = x + 1
            if x in rightBorder or x > 587*817:
                break
        if len(path) == 587:
            count = count + 1
            # profile.append(path)
            f.writelines(str(path))
            f.writelines("\n")


        # 右下
        path = []
        x = index
        for i in range(587):
            path.append(x)
            x = x + 818
            if x > 587*817:
                break
        if len(path) == 587:
            count = count + 1
            # profile.append(path)
            f.writelines(str(path))
            f.writelines("\n")

        # 下
        path = []
        x = index
        for i in range(587):
            path.append(x)
            x = x + 817
            if x > 587*817:
                break
        if len(path) == 587 and x != 479579 :
            count = count + 1
            # profile.append(path)
            f.writelines(str(path))
            f.writelines("\n")

print("count:",count)