#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 求两个数字之间的素数
# 素数：质数定义为在大于1的自然数中，除了1和它本身以外不再有其他因数。只能被1及自己整除的数，如3，7，13，23等

def prime(a, b):
    prime_list = [x for x in range(a, b) if 0 not in [x%y for y in range(2, x)]]
    return prime_list

print(prime(2,30))
