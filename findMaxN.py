#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 递归找出列表中最大的数字

def findMaxN(alist):
	if len(alist) == 0:
		return None
	elif len(alist) == 1:
		return alist[0]
	else:
		sub_max = findMaxN(alist[1:])
		return alist[0] if alist[0] > sub_max else sub_max

print(findMaxN([1,2,3,5,7,8]))
