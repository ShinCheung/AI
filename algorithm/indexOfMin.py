#!/usr/bin/env python
# -*- coding: utf-8 -*-

def indexOfMin(alist):
	minIndex = 0
	curIndex = 1
	while curIndex < len(alist):
		if alist[curIndex] < alist[minIndex]:
			minIndex = curIndex
		curIndex += 1
	return minIndex

test = [1,8,1,-1,4,7,2,-2,99]
print(indexOfMin(test))

