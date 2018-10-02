#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 给定一个数组a （可能包含相同的数），求它有多少个不同的子序列。
# 例如a=[1,2,1,3]
# 子序列有 {1} {2} {3} {1,2} {1,3} {1,2} {1,1} {1,3} {2, 1} {2,3} {1,2,1} {1,2,3} {1,1,3} {2,1,3} 等。

def alist(a):
    ls = []
    for i in range(len(a)):
        for j in range(i+1,len(a)+1):
            if a[i:j] not in ls:
                # print(a[i:j])
                ls.append(a[i:j])
    return ls

a=[1,2,1,3]
print(alist(a))