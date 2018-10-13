#!/usr/bin/env python
# -*- coding: utf-8 -*-

def merge_list(*args):
    s = set()
    for i in args:
        s = s.union(i)
    return s

alist = ['a','b','c','d','e','f']
blist = ['x','y','z','e','f']
print(merge_list(alist, blist))

