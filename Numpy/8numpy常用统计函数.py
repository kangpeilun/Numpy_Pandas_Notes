# -*- coding: utf-8 -*-
# date: 2021/11/1
# Project: Numpy_Pandas_Notes
# File Name: 8numpy常用统计函数.py
# Description: 
# Author: Anefuer_kpl
# Email: 374774222@qq.com

import numpy as np

t1 = np.array([[1,2,3],[4,5,6]])
t2 = np.array([[1,2,3],[4,5,6]])
t3 = np.array([[1,2,3],[4,5,6]])

print('==========================求和==============================')
print(t1.sum(axis=0))  # 按行方向求和
print(t1.sum(axis=1))  # 按列方向求和
print(t1.sum())  # 所有元素求和

print('==========================求均值==============================')
print(t2.mean(axis=0)) # 按行方向求均值
print(t2.mean(axis=1)) # 按列方向求均值
print(t2.mean()) # 所有元素求均值

print('==========================求中位数==============================')
print(np.median(t3, axis=0)) # 按行方向求中位数
print(np.median(t3, axis=1)) # 按列方向求中位数
print(np.median(t3)) # 所有元素求中位数

print('==========================求最大值==============================')
print(t2.max(axis=0)) # 按行方向求均值
print(t2.max(axis=1)) # 按列方向求均值
print(t2.max()) # 所有元素求均值

print('==========================求最小值==============================')
print(t2.min(axis=0)) # 按行方向求均值
print(t2.min(axis=1)) # 按列方向求均值
print(t2.min()) # 所有元素求均值

print('==========================求极值(最大值和最小值的差)==============================')
print(np.ptp(t3, axis=0)) # 按行方向求中位数
print(np.ptp(t3, axis=1)) # 按列方向求中位数
print(np.ptp(t3)) # 所有元素求中位数

print('==========================求标准差(一组数据平均值分散程度)==============================')
'''
    一个较大的标准差，代表大部分数值和其平均值之间差异较大
    一个较小的标准差，代表这些数值较接近平均值，反映出数据的波动越稳定
    标准差越大，波动越大，越不稳定
'''
print(t2.std(axis=0)) # 按行方向求均值
print(t2.std(axis=1)) # 按列方向求均值
print(t2.std()) # 所有元素求均值