#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 顺时针打印矩阵
def printMatrix(matrix):
        # write code here
        res=[]
        n=len(matrix)   # 行的长度
        m=len(matrix[0])    # 列的长度
        if n==1 and m==1:
            res=[matrix[0][0]]
            return res
        for o in range((min(m,n)+1)//2):
            [res.append(matrix[o][i]) for i in range(o,m-o)]
            [res.append(matrix[j][m-1-o]) for j in range(o,n-o) if matrix[j][m-1-o] not in res]
            [res.append(matrix[n-1-o][k]) for k in range(m-1-o,o-1,-1) if matrix[n-1-o][k] not in res]
            [res.append(matrix[l][o]) for l in range(n-1-o,o-1,-1) if matrix[l][o] not in res]
        return res

# 法二：将已经走过的地方置0，然后拐弯的时候判断一下是不是已经走过了，如果走过了就计算一下新的方向
def spiralOrder(matrix):
    r, i, j, di, dj = [], 0, 0, 0, 1
    if matrix != []:
        for _ in range(len(matrix) * len(matrix[0])):
            r.append(matrix[i][j])
            matrix[i][j] = 0
            if matrix[(i + di) % len(matrix)][(j + dj) % len(matrix[0])] == 0:
                di, dj = dj, -di
            i += di
            j += dj
    return r

a = [
    [1,2,3,4],
    [5,6,7,8],
    [9,10,11,12],
    [13,14,15,16]
]
print(printMatrix(a))
print(spiralOrder(a))
