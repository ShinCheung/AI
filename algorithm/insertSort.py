#!/usr/bin/env python
# -*- coding: utf-8 -*-

def insertSort(alist):
    for key, item in enumerate(alist):
        index = key
        while index > 0 and alist[index-1] > item:
            alist[index] = alist[index-1]
            index -= 1
        alist[index] = item
    return alist

alist = [54,26,93,17,77,31,44,55,20]
print(insertSort(alist))

def insertSort2(alist):
    for index in range(1, len(alist)):
        currentvalue = alist[index]
        position = index

        while position > 0 and alist[position-1] > currentvalue:
            alist[position] = alist[position-1]
            position -= 1
        alist[position] = currentvalue
    return alist

print(insertSort2(alist))
