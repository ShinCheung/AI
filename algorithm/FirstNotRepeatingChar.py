#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 找到第一个只出现一次的字符,并返回它的位置, 如果没有则返回 -1（需要区分大小写）

def FirstNotRepeatingChar(s):
    if not s:
        return -1
    for k,v in enumerate(s):
        if s.count(v) == 1:
            return k

ch='google'
print(FirstNotRepeatingChar(ch))