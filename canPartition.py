#!/usr/bin/env python
# -*- coding: utf-8 -*-

def canPartition(nums):
    length = len(nums)
    mySum =  sum(nums)
    if mySum % 2 == 1:
        return False
    mySum //= 2
    dp = [False for x in range(20000)]
    dp[0] = True
    for i in range(0,length):
        for j in range(mySum, nums[i] - 1, -1):
            dp[j] |= dp[j - nums[i]]
    return dp[mySum]

test = [1, 5, 11, 5]
print(canPartition(test))

