#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 1 到 n 中1出现的次数
# eg:1~13中包含1的数字有1、10、11、12、13因此共出现6次

def NumberOf1Between1AndN_Solution(n):
    if n < 1:
        return 0
    # map特殊用法,int转str,range从0开始到n-1 => 需要+1
    a = list(map(str,range(n+1)))
    ones = [i for i in a if '1' in i]
    return ''.join(ones).count('1')

print(NumberOf1Between1AndN_Solution(13))
