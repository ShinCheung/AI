# 最长公共序列
# 首先获得打分矩阵：通过动态规划的编程思想，比较两序列的字符，确定打分矩阵中每个元素的数值。
# 初始化矩阵
# c[i,0]=0和c[0,j]=0
# 计算若两字符相同则c[i,j]=c[i-1,j-1]+1,否则为c[i-1,j],c[i,j-1]的最大值。
# 在计算打分矩阵的同时，加入方向矩阵的生成，方向矩阵一般用于回溯
import numpy as np
def LCS(x,y):
    c = np.zeros((len(x)+1,len(y)+1))
    b = np.zeros((len(x)+1,len(y)+1))
    for i in range(1,len(x)+1):
        for j in range(1,len(y)+1):
            if x[i-1] == y[j-1]:
                c[i,j] = c[i-1,j-1] + 1
                b[i,j] = 2
            else:
                if c[i-1,j] >= c[i,j-1]:
                    c[i,j] = c[i-1,j]
                    b[i,j] = 1
                else:
                    c[i,j] = c[i,j-1]
                    b[i,j] = 3
    return c, b
# 接下来构建回溯方法：回溯方法根据方向矩阵的数值，若为2，则表示为共有元素，需要保存，回溯完整个矩阵后，结束，输出结果。
def getLCS(x,y):
    _, b = LCS(x,y)
    i = len(x)
    j = len(y)
    lcs = ''
    while i > 0 and j > 0:
        if b[i][j] == 2:
            lcs = x[i-1] + lcs
            i -= 1
            j -= 1
        if b[i][j] == 1:
            i -= 1
        if b[i][j] == 3:
            j -= 1
        if b[i][j] == 0:
            break
    return lcs

# print(LCS('ABCBDAB', 'BDCABA'))
print(getLCS('ABCBDAB', 'BDCABA'))