# -*- coding: utf-8 -*-
# date: 2021/11/1
# Project: Numpy_Pandas_Notes
# File Name: 2.数组的形状.py
# Description: 
# Author: Anefuer_kpl
# Email: 374774222@qq.com

import numpy as np

'''
    切记：有几个数就表示 几维
'''
t1 = np.arange(12)
print(t1.shape)

t2 = np.array([
    [1,2,3],
    [4,5,6]
])
print(t2.shape)

t3 = np.array([
    [[1,2,3]],
    [[4,5,6]]
])
print(t3.shape)

# ====================reshape修改形状，数组本身不会发生变化========================
t4 = np.arange(12)
t5 = t4.reshape([3,4])
print('t5',t5)
'''
    如果数组是一个三维的，这样理解每个维度的含义
    第一个维度表示：块
    第二个维度表示：每个块中有几行
    第三个维度表示：每个块中有几列
'''
t6 = t4.reshape([2,2,3])
print('t6',t6)
print('t6 size',t6.size)  # 查看数组一共有多少个元素 !!!
t7 = t6.reshape((t6.size))  # 将数组 变成一维的
print('t7',t7)
t8 = t6.flatten()  # 将数组 变成一维的 !!!
print('t8', t8)