#!/usr/bin/env python
# -*- coding: utf-8 -*-

#1
def quickSort(L, low, high):
    if low < high:
        left, right = low, high
        # 设置基准数
        base = L[low]
        while left < right:
            # 如果列表后边的数,比基准数大或相等,则前移一位直到有比基准数小的数出现
            while left < right and L[right] >= base:
                right = right - 1
            L[left] = L[right]
            while left < right and L[left] <= base:
                left = left + 1
            L[right] = L[left]
        # 做完第一轮比较之后,列表被分成了两个半区,并且left=right,需要将这个数设置回base
        L[left] = base
        # 递归前后半区
        quickSort(L, low, left - 1)
        quickSort(L, left + 1, high)
    return L

# test = [6,5,5,6,1,3,2,4,8,7,6,0,9,5]
# print(quickSort(test, 0, len(test)-1))

#2
def quicksort(array):
    if len(array) < 2:  # 基线条件：为空或只包含一个元素的数组是有序的
        return array
    else:
        pivot = array[0]    # 递归条件
        less = [i for i in array[1:] if i <= pivot]     # 发现不加等号，相当于排序去重
        greater = [i for i in array[1:] if i > pivot]
        return quicksort(less) + [pivot] + quicksort(greater)

test = [6,5,5,6,1,3,2,4,8,7,6,0,9,5]
print(quicksort(test))