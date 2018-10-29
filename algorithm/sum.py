#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 求两个整数之和，要求在函数体内不得使用+、-、*、/四则运算符号

# 位运算，三步走：
# 1、不考虑进位相加相当于异或
# 2、与运算左移一位
# 3、重复前两部，直到不产生进位
def Add(num1, num2):
    while num2 != 0:
        Sum=num1^num2
        carry=(num1&num2)<<1
        num1=Sum
        num2=carry
    return num1

def add(num1, num2):
    return sum([num1,num2])

print(Add(3,5))
print(add(3,5))