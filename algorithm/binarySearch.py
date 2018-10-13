#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 实现一个二分查找
# 输入:一个顺序list
# 输出: 待查找的元素的位置

def binarySearch(sortedList, target):
	left = 0
	right = len(sortedList) - 1
	while left <= right:
		mid = (left+right)//2
		if sortedList[mid] < target:
			left = mid + 1
		elif sortedList[mid] > target:
			right = mid - 1
		else:
			return mid + 1 		# sortedList[mid] == target的情况；显示位置，不加1则从0开始数，加1从1开始
	return -1

test = [0,1,2,5,6,8,10,12,16]
print(binarySearch(test, 5))
