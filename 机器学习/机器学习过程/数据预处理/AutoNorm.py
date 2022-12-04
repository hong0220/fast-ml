# -*- coding: UTF-8 -*-

# 矩阵宽度
def width(lst):
    i = 0
    # 数组长度
    for j in lst[0]:
        i = i + 1
    return i


def AutoNorm(mat):
    m = width(mat)

    # 最大值
    MaxNum = [0] * m
    for i in mat:
        for j in range(0, m):
            if i[j] > MaxNum[j]:
                MaxNum[j] = i[j]

    # 最小值
    MinNum = [9999999999] * m
    for p in mat:
        for q in range(0, m):
            if p[q] <= MinNum[q]:
                MinNum[q] = p[q]

    section = list(map(lambda x: x[0] - x[1], zip(MaxNum, MinNum)))
    print(section)
    NormMat = []

    # y=(x-min)/(max-min)
    # 特例处理,todo
    for k in mat:
        distance = list(map(lambda x: x[0] - x[1], zip(k, MinNum)))
        value = list(map(lambda x: x[0] / x[1], zip(distance, section)))
        NormMat.append(value)
    return NormMat
