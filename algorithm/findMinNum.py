#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 把数组排成最小的数
# 输入一个正整数数组，把数组里所有数字拼接起来排成一个数，打印能拼接出的所有数字中最小的一个。
# 例如输入数组[3,32,321]，则打印出这三个数字能排成的最小数字为321323

import itertools

def PrintMinNumber(numbers):
        if not numbers:
            return ''
        nums = []
        list_num = list(itertools.permutations(numbers,len(numbers)))
        for item in list_num:
            num = ''.join(map(str,item))
            nums.append(num)
        return min(map(int,nums))

test=[3,32,321]
print(PrintMinNumber(test))