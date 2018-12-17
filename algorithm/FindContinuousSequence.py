#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 和为s的连续正数序列

def FindContinuousSequence(tsum):
    if tsum < 3:
        return []
    small, big = 1, 2
    curSum = small + big
    res = []
    while small < big:
        if curSum == tsum:
            res.append(list(range(small,big + 1)))
            big += 1
            curSum += big
        elif curSum >= tsum:
            curSum -= small
            small += 1
        else:
            big += 1
            curSum += big
    return res

print(FindContinuousSequence(15))
