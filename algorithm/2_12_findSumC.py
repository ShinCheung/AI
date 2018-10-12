#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 快速找到数组中两数之和等于一给定的值

# 穷举
def findSumC1(alist, c):
    alist = sorted(alist)
    a = 0
    b = len(alist)-1
    result = []
    while a < b:
        sumab = alist[a] + alist[b]
        if sumab == c:
            result.append((alist[a],alist[b]))
            a += 1	# a+1（右移）或b-1（左移），为了保证a+b=c所有的情况
        elif sumab < c:
            a += 1
        else:
            b -= 1
    return result

# 哈希
def findSumC2(alist, c):
    adict = {}
    result = []
    for item in alist:
        adict[item] = 1
    for item in alist:
        if c-item < item:
            break
        if c-item in adict:
            result.append((item, c-item))
    return result

alist = [1,5,6,7,8,9]
print(findSumC2(alist, 10))
