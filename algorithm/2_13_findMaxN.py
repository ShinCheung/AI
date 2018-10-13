#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 求子数组的最大乘积:N维数组,找一个子数组N-1维,使得数组乘积最大，只能用乘法

from functools import reduce

# 法一：从低到高，排除那个i，计算剩下的乘积
def findMaxN1(alist):
    result = 0
    for i in range(len(alist)):
        tmp = reduce(lambda x, y : x * y, alist[:i] + alist[i+1:])
        if tmp > result:
            result = tmp
    return result

# 法二：计算整个乘积P,P=0,>0,<0三种情况
def findMaxN2(alist):
    P = reduce(lambda x, y : x * y, alist)
    if P == 0:
        i = alist.index(0)
        Q = reduce(lambda x, y : x * y, alist[:i] + alist[i+1:])
        if Q == 0:
            tmp = 0
        else:
            tmp = Q
    elif P > 0:
        if i == alist.index(min([item for item in alist if item > 0])):
            tmp = reduce(lambda x, y : x * y, alist[:i] + alist[i+1:])
        if i == alist.index(max([item for item in alist if item < 0])):
            tmp = reduce(lambda x, y : x * y, alist[:i] + alist[i+1:])
    else:
        i = alist.index(max([item for item in alist if item < 0]))
        tmp = reduce(lambda x, y : x * y, alist[:i] + alist[i+1:])
    return tmp

alist = [1,2,0,3,4]
print(findMaxN1(alist))

