#!/usr/bin/env python
# -*- coding: utf-8 -*-

from heapq import merge

def mergeSort(alist):
    if len(alist) <= 1:
        return alist
    mid = len(alist)//2
    left = mergeSort(alist[:mid])
    right = mergeSort(alist[mid:])
    # return merge(left, right)
    return list(merge(left, right))
 
# def merge(left, right):
#     result=[]
#     while len(left) > 0 and len(right) > 0:
#         if left[0] < right[0]:
#             result.append(left.pop(0))
#         else:
#             result.append(right.pop(0))
#     result += left
#     result += right
#     return result

alist = [54,26,93,17,77,31,44,55,20]
print(mergeSort(alist))
