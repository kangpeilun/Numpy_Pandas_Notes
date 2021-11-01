# -*- coding: utf-8 -*-
# date: 2021/11/1
# Project: Numpy_Pandas_Notes
# File Name: 3布尔索引.py
# Description: 
# Author: Anefuer_kpl
# Email: 374774222@qq.com

import pandas as pd
import numpy as np

t1 = pd.DataFrame(np.arange(12).reshape(3,4), index=list('abc'), columns=list('WXYZ'))

'''
    t1['W']>2 的返回值是布尔数组
    a    False
    b     True
    c     True
    
    t1[t1['W']>2] 会取出所有布尔值为True的结果
'''
print(t1['W']>2)
print(t1[t1['W']>2]) # 按照W列的运算结果，取出对应的行。 获取W列所有大于2 的行

print('===================================多个条件 锁定范围=====================================')
'''
    PS: & | 连接的多个条件一定要用小括号'()' 包住
'''
# 与 操作
print(t1[(t1['W']>1) & (t1['W']<5)])  # 获取W列的数据 大于1 且 小于5 的所有行
print(t1[(t1['W']>1) & (t1['Z']<9)])  # 获取W列的数据 大于1 且 Z列小于9 的所有行
# 或 操作
print(t1[(t1['W']>1) | (t1['W']<5)])  # 获取W列的数据 大于1 或 小于5 的所有行
print(t1[(t1['W']>1) | (t1['Z']<9)])  # 获取W列的数据 大于1 或 Z列小于9 的所有行

print('===================================字符串方法(类似python中的操作)=====================================')
temp = {
    'W':['a/v/c', 'asd asd', 'asdasd/123/AASD'],
    'X':['a/v/c', 'asd asd', 'asdasd/123/AASD'],
    'Y':['a/v/c', 'asd asd', 'asdasd/123/AASD'],
    'Z':['a/v/c', 'asd asd', 'asdasd/123/AASD'],
}
t2 = pd.DataFrame(temp, index=list('abc'))
t3 = pd.DataFrame(temp, index=list('abc'))
print(t2)
'''
    .tolist()  将DataFrame数据类型转换为列表
'''
print(t2['W'].str.split('/').tolist())  # .str.split('/') 将字符串根据 '/' 进行分割
print(t2['W'].str.len())  # .str.len() 计算每个字符串的长度
print(t2['W'].str.upper()) # .str.upper() 将 W 列每个字母变为大写
print(t2['W'].str.lower()) # .str.upper() 将 W 列每个字母变为小写
print(t2['W'].str.replace('/', '@')) # .str.replace('/', '@') 将 W 列每个字符串中的'/'替换为'@'


