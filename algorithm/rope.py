#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 数轴上从左到右有n个点a[0],a[1]...a[n-1],给定一根长度为L的绳子，求绳子最多能覆盖其中的几个点。

def calculate(alist,n,L):
    i,best = 0,0
    while i + best < n and alist[i+best] - alist[i] <= L:
        best += 1
    i+=1
    return best

alist = [1,5,8,12,36,50,58]
n = 7
L = 51
print(calculate(alist,n,L))
