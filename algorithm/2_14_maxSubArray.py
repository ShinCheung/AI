#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 求数组中连续项之和的最大值

def maxSubArray(alist):
	for i in range(1, len(alist)):
		if alist[i - 1] > 0:
			alist[i] += alist[i - 1]
	return max(alist)

# alist1 = [1,-2,3,5,-3,2]		# 8
alist2 = [0,-2,3,5,-1,2]		# 9
# alist3 = [-9,-2,-3,-5,-3]		# -2
# print(maxSubArray(alist1))
print(maxSubArray(alist2))
# print(maxSubArray(alist3))
