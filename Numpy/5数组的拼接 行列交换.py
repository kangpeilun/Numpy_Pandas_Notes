# -*- coding: utf-8 -*-
# date: 2021/11/1
# Project: Numpy_Pandas_Notes
# File Name: 5数组的拼接 行列交换.py
# Description: 
# Author: Anefuer_kpl
# Email: 374774222@qq.com

import numpy as np

t1 = np.array([[1,2,3], [4,5,6]])
t2 = np.array([[10,11,12], [13,14,15]])

t3 = np.vstack((t1, t2))  # 将t1和t2在竖直方向上拼接
'''
    [[ 1  2  3]
     [ 4  5  6]
     [10 11 12]
     [13 14 15]]
'''
t4 = np.hstack((t1, t2))  # 将t1和t2在水平方向上拼接
'''
    [[ 1  2  3 10 11 12]
     [ 4  5  6 13 14 15]]
'''
print(t3)
print(t4)

print('=============================数组行列进行交换=================================')
t1[:,[0,1]] = t1[:, [1,0]]  # 将t1的第1，2列交换
print(t1)
t1[[0,1],:] = t1[[1,0], :]  # 将t1的第1，2行交换
print(t1)