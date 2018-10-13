#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 最长递增子序列的长度，连续不连续都满足
def LIS(alist):
    n = len(alist)
    dp = [1] * n
    for i in range(1, n):
        if alist[i] > alist[i - 1]:
            dp[i] = dp[i - 1] + 1
        else:
            dp[i] = dp[i - 1]
    return max(dp)
    # return dp[-1]

# 求数组中最大子序列的和，子序列可以不连续
def test_func(alist):
    n = len(alist)
    dp = [0] * n
    for i in range(n):
        dp[i] = max(dp[i-1] + alist[i], dp[i-1])
    return max(dp)
    # return dp[-1]

# 最大和的"连续"子数组，强调必须连续 有难度
def maxSubArray(alist):  
    n = len(alist)
    for i in range(1, n):
        # 当前值的大小与前面的值之和比较，若当前值更大，则取当前值，舍弃前面的值之和  
        subMaxSum = max(alist[i] + alist[i-1], alist[i])
        alist[i] = subMaxSum    # 将当前和最大的赋给alist[i]，新的alist存储的为和值  
    return max(alist)

test = [1,-1,2,-3,4,-5,6,-7]
alist = [-2,1,-3,4,-1,2,1,-5,4]
print(LIS(test))    # [1，2，4，6]
print(test_func(test))
print(maxSubArray(alist))    # [4,-1,2,1]
