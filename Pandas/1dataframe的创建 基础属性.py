# -*- coding: utf-8 -*-
# date: 2021/11/1
# Project: Numpy_Pandas_Notes
# File Name: 1dataframe的创建 基础属性.py
# Description: 
# Author: Anefuer_kpl
# Email: 374774222@qq.com

import pandas as pd
import numpy as np

'''
    DataFrame对象既有行索引，又有列索引
    行索引 index：axis=0
    列索引 columns：axis=1
'''
t1 = pd.DataFrame(np.arange(12).reshape(3,4))
'''
       0  1   2   3
    0  0  1   2   3
    1  4  5   6   7
    2  8  9  10  11
'''
print(t1)

# 给DataFrame指定index和columns
t2 = pd.DataFrame(np.arange(12).reshape(3,4), index=list('abc'), columns=list('WXYZ'))
print(t2)

print('===================================基础属性=====================================')
print(t2.shape)  # 行数 列数  (3, 4)
print(t2.dtypes) # 列数据类型
'''
    W    int32
    X    int32
    Y    int32
    Z    int32
'''
print(t2.ndim) # 数据维度  2
print(t2.index) # 行索引  Index(['a', 'b', 'c'], dtype='object')
print(t2.columns) # 列索引 Index(['W', 'X', 'Y', 'Z'], dtype='object')
print(t2.values) # 对象值，二维ndarray类型
'''
    [[ 0  1  2  3]
     [ 4  5  6  7]
     [ 8  9 10 11]]
'''
print('===================================整体情况查询=====================================')
print(t2.head(2))  # 显示头部几行，默认5行
print(t2.tail(2))  # 显示末尾几行，默认5行
print(t2.info()) # 相关信息：行数，列数，列索引，列非空值个数，列类型，内存占用
print(t2.describe()) # 快速综合统计结果：计数，均值，标准差，最大值，四分位数，最小值

print('===================================根据某一列进行排序排序方法=====================================')
t3 = t2.sort_values(by='W', ascending=False)  # 根据W列的属性值进行排序。ascending默认为True 升序排序
print(t3)