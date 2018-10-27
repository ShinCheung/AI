#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 找出出现次数超过数组长度的一半数字

# import collections
from collections import Counter

a=[1,2,3,2,2,2,5,4,2]
# tmp=collections.Counter(a)
tmp=Counter(a)
l=len(a)//2
for k,v in tmp.items():
    # print(k,v)
    if v > l:
        print(k)
