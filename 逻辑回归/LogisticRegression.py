# -*- coding: UTF-8 -*-

import matplotlib.pyplot as plt
from numpy import *


def plotBestFit(weights):
    dataMat, labelMat = loadDataSet()

    dataArray = array(dataMat)
    xCord1 = []
    yCord1 = []
    xCord2 = []
    yCord2 = []
    n = shape(dataArray)[0]
    for i in range(n):
        if int(labelMat[i]) == 1:
            xCord1.append(dataArray[i, 1]);
            yCord1.append(dataArray[i, 2])
        else:
            xCord2.append(dataArray[i, 1]);
            yCord2.append(dataArray[i, 2])

    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.scatter(xCord1, yCord1, s=30, c='red', marker='s')
    ax.scatter(xCord2, yCord2, s=30, c='green')

    # todo
    x = arange(-3.0, 3.0, 0.1)
    # y = (0.48 * x + 4.12414) / (-0.616)
    # y = (weights[0] + weights[1] * x) / (-weights[2])
    y = (float(weights[0][0]) + float(weights[1][0]) * x) / -float(weights[2][0])
    ax.plot(x, y)

    plt.xlabel('X1')
    plt.ylabel('X2')
    plt.show()


def loadDataSet():
    dataMat = []
    labelMat = []
    file = open('/Users/hongduoduo/Desktop/fast-ml/DataSet/testSet-LR.txt')
    for line in file.readlines():
        lineArray = line.strip().split()
        dataMat.append([1.0, float(lineArray[0]), float(lineArray[1])])
        labelMat.append(int(lineArray[2]))
    return dataMat, labelMat


def sigmoid(inX):
    return 1.0 / (1 + exp(-inX))


def gradAscent(dataMatIn, classLabels):
    # 特征列
    dataMatrix = mat(dataMatIn)
    # 目标列
    labelMat = mat(classLabels).transpose()

    m, n = shape(dataMatrix)
    # 每次迭代的步长
    alpha = 0.001
    weights = ones((n, 1))

    maxCycles = 500
    for k in range(maxCycles):  # heavy on matrix operations
        h = sigmoid(dataMatrix * weights)
        error = (labelMat - h)  # vector subtraction
        weights = weights + alpha * dataMatrix.transpose() * error
    return weights


def GetResult():
    dataMat, labelMat = loadDataSet()
    weights = gradAscent(dataMat, labelMat)
    print(weights)
    plotBestFit(weights)


if __name__ == '__main__':
    GetResult()
