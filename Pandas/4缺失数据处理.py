# -*- coding: utf-8 -*-
# date: 2021/11/1
# Project: Numpy_Pandas_Notes
# File Name: 4缺失数据处理.py
# Description: 
# Author: Anefuer_kpl
# Email: 374774222@qq.com

import pandas as pd
import numpy as np

temp = {
    'W': [np.nan, 123, 'asd/asd'],
    'X': ['123', np.nan, 'asd/asd'],
    'Y': [np.nan, 123, 'asd/asd'],
    'Z': [np.nan, 123, np.nan,],
}

t1 = pd.DataFrame(temp, index=list('abc'))
print(t1)

# 判断数据是否为NaN
print(t1.isna())
# 判断数据哪些 不为 NaN
print(t1.notna())

print('==========================缺失值处理方式=============================')
print('==========================1.删除NaN所在的行 或 列=============================')
'''
    axis=0 按行进行删除
    how='any' 只要该行有NaN 就删除该行, 默认为'any'
    how='all' 当该行所有元素都为NaN 才删除该行
    inplace=False 是否进行就地修改, 默认为'False'表示不进行就地修改
'''
print(t1.dropna(axis=0, how='any', inplace=False))
print(t1.dropna(axis=0, how='all', inplace=False))

print('==========================2.在NaN处填充数据=============================')
'''
    .fillna(10) # 在NaN位置处填充上10
    t1.mean() 会计算每一列的 平均值。 PS: 不会把 NaN 所在的行算进去
'''
print(t1.fillna(t1.mean()))  # 每一列都根据其 除了NaN之外的数据计算的 平均值 进行填充
print(t1['Z'].fillna(t1['Z'].mean()))
t1['Z'] = t1['Z'].fillna(t1['Z'].mean()) # 仅对某列进行填充。把 第Z列的 平均值填充到 第Z列中
print(t1)