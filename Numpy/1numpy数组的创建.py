# -*- coding: utf-8 -*-
# date: 2021/11/1
# Project: Numpy_Pandas_Notes
# File Name: 1numpy数组的创建.py
# Description: 
# Author: Anefuer_kpl
# Email: 374774222@qq.com

import numpy as np
from random import random

# ==========================使用numpy生成数组===============================
t1 = np.array([1,2,3,4])
print('t1',t1)

# 两者结果一样
t2 = np.array(range(10))
print('t2',t2)
t3 = np.arange(10)
print('t3',t3)

# ==========================numpy中的数据类型===============================
t4 = np.array(range(1,4), dtype=float)  # 指定数据类型
print('t4',t4)
# ==========================调整数据类型===============================
t5 = t4.astype('int64')
print('t5',t5)
# ==========================保留小数后几位===============================
t6 = np.array([random() for i in range(10)])
t7 = np.round(t6, 2)  # 保留 两位 小数, 后面数字为保留的位数
print('t6', t6)
print('t7', t7)
