#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 求按从小到大的顺序的第N个丑数。能被2、3、5整除
# 丑数应该是另一个丑数乘以2、3、5的结果（1除外）,可以创建一个数组用于存排好序的丑数
# 思路关键是怎样确保数组里面的丑数是排好序的，如16行所示

def getUglyNumber(index):
        if index <= 0:
            return 0
        uglyList = [1]
        index2,index3,index5 = 0,0,0
        for _ in range(index-1):
            newUgly = min(uglyList[index2]*2, uglyList[index3]*3, uglyList[index5]*5)
            uglyList.append(newUgly)
            if newUgly % 2 == 0:
                index2 += 1
            if newUgly % 3 == 0:
                index3 += 1
            if newUgly % 5 == 0:
                index5 += 1
        return uglyList[-1]

print(getUglyNumber(1500))