# -*- coding: utf-8 -*-
# date: 2021/11/1
# Project: Numpy_Pandas_Notes
# File Name: 7numpy中的nan和inf.py
# Description: 
# Author: Anefuer_kpl
# Email: 374774222@qq.com

'''
    切记：numpy中将nan当作float类型处理的
    nan: not a number 表示不是一个数字
        当读取本地文件为float时，若有缺失值，则会出现nan
        当做了一个不合适的运算时，如：0/0=nan, inf-inf=nan

    inf: infinity 表示无穷   -inf: 表示负无穷
        当一个数字除以0（python会直接报错，numpy会是一个inf 1/0=inf）

    numpy中nan的注意事项：
        1.两个nan是不相等的  np.nan != np.nan
        2.利用以上特性，判断数组中nan的个数
        3.使用np.isnan()判断一个float是否为nan，返回bool类型
        4.nan和任何值计算都为nan
'''
import numpy as np

print(np.nan == np.nan)

t1 = np.array([1,2,3, np.nan, np.nan])
print(t1)
'''
    统计两个数组中 不相同元素 的个数
    因为两个np.nan 是不相等的，那么就可以统计出来当前数组中nan的个数
'''
print(np.count_nonzero(t1!=t1))
print(t1+np.nan)

print('============================numpy中的统计方法=============================')
t2 = np.array([[1,2,3], [4,5,6]])
print(np.sum(t2, axis=0))  # 按 行方向 进行相加，最终呈现的效果是，每一列 上的数字进行求和
print(np.sum(t2, axis=1))  # 按 列方向 进行相加，最终呈现的效果是，每一行 上的数字进行求和