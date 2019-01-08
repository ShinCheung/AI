#!/usr/bin/env python
# -*- coding: utf-8 -*-

def findKMin(alist, k):
        if not alist:
            return
        n = len(alist)
        if n < k:
            return
        alist = sorted(alist)
        return alist[:k]

alist=[1,2,3,4,5,6,7,8,9]
print(findKMin(alist, 3))
