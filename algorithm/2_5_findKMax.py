#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 寻找最大的K个数

def partion(alist):
    a = alist[len(alist)//2]
    Sa = []
    Sb = []
    for item in alist:
        if item >= a:
            Sa.append(item)
        else:
            Sb.append(item)
    return (Sa, Sb)

def findKMax(alist, k):
    if k <= 0:
        return []
    if len(alist) <= k:
        return alist
    Sa, Sb = partion(alist)

    a = findKMax(Sa, k)
    b = findKMax(Sb, k-len(Sa))
    return a + b

# 直接使用sorted取最后k大的数即可
def findKMax2(alist, k):
    return sorted(alist)[-k:]

alist = [1,2,3,4,5,6,7,8,9]
print(findKMax(alist, 6))
print(findKMax2(alist, 6))
