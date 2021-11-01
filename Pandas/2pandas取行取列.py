# -*- coding: utf-8 -*-
# date: 2021/11/1
# Project: Numpy_Pandas_Notes
# File Name: 2pandas取行取列.py
# Description: 
# Author: Anefuer_kpl
# Email: 374774222@qq.com

import pandas as pd
import numpy as np

t1 = pd.DataFrame(np.arange(12).reshape(3,4), index=list('abc'), columns=list('WXYZ'))
'''
    方括号内：
        如果直接传入的数字，那么是根据 行索引进行取值
        如果传入的是字符串，那么是根据 列索引进行取值
'''
print(t1[:1])  # 取第2行之前的所有行 (左闭右开原则)
print(t1['W']) # 取索引名为 W 的一整列
print(t1[:1]['W']) # 取第2行之前的所有行 和 W列

'''
    PS: 通过索引获取数据，支持对连续多行的查找
    df.loc[行标签, 列标签]  通过标签(字符串名)获取数据
    df.iloc[行索引, 列索引] 通过索引获取数据
'''
print(t1.loc['a','W'])  # 获取行标签为a, 列标签为W 的数据
print(t1.loc[['a', 'c'], ['W', 'Z']])  # 根据标签获取多行 行索引，列索引 的数据。 获取a c行，W Z列的数据

print(t1.iloc[1,2]) # 取第2行 第3列的 数据
print(t1.iloc[[0,1], [1,3]]) # 取多行多列。 获取第1 2行 第2 4列的数据
print(t1.iloc[1:, 0:2])  # 取连续的多行多列。 获取第1行之后的所有行，第1 2列 (左闭右开)