#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 数组循环移位
# [abcd1234]算法的核心是:交换abcd,1234的位置，如何交换呢，可以用三次逆序实现:
# 1.abcd 逆:[dcba1234]
# 2.1234 逆:[dcba4321]
# 3.全逆:   [1234abcd]
# 用三次旋转实现，线性时间，但是只使用一个旋转用的变量

# N > 0左移N位，N < 0右移N位
def leftMoveN(alist, N):
    N = N % len(alist)
    alist[:N] = list(reversed(alist[:N]))
    alist[N:] = list(reversed(alist[N:]))
    return list(reversed(alist))
    # return alist[::-1]

# 法一简化版
def leftMoveN2(alist, N):
    N = N % len(alist)
    return (alist[:N][::-1] + alist[N:][::-1])[::-1]

#############################################################

# offset>0右移；offset<0左移
def rotateString(s, offset):
    if len(s) > 0:
        offset = offset % len(s)
    temp = (s + s)[len(s) - offset : 2 * len(s) - offset]
    # print(temp)
    for i in range(len(temp)):
        s[i] = temp[i]
    return s

test = ['a','b','c','d',1,2,3,4]
print(leftMoveN(test, 1))
print(leftMoveN2(test, 1))
print(rotateString(test, 1))
