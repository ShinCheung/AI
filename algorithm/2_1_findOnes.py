#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 求二进制数字中1的个数

#1.求余数的方法:除2取余
def findOnes(num):
	sum_one = 0
	while num:
		sum_one += num%2
		num = num//2
	return sum_one

#2.位操作方法，思路同上，只是表述不一样
def findOnes2(num):
    sum_one=0
    while num:
        sum_one += num & 0x01
        num = num>>1
    return sum_one

#3.位操作，基于这样的常用方法：使得一个二进制数a最低的1变成0方法是；a＝a&（a-1）
def findOnes3(number):
    sum_one=0
    while number:
        number=number&(number-1)
        print(number)
        sum_one+=1
    return sum_one

# bin(n) 是python的一个系统函数，能够将n 转换为 0b110001 的二进制形式
def countBits1(n):
    return len(bin(n).replace("0b","").replace("0",""))

def countBits2(n):
    return bin(n).count("1")

print(findOnes3(15))

