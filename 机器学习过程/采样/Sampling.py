# -*- coding: UTF-8 -*-

import random


# 无放回随机抽样
def RandomSampling(dataMat, number):
    try:
        return random.sample(dataMat, number)
    except:
        print('sample larger than population')


# 放回随机抽样
def RepetitionRandomSampling(dataMat, number):
    sample = []
    for i in range(number):
        sample.append(dataMat[random.randint(0, len(dataMat) - 1)])
    return sample


# 系统抽样(等距抽样)，无放回抽样
# 适用于按照一定关系排列好的数据，照顾每个小分类的样本数据。
def SystematicSampling(dataMat, number):
    sample = []
    i = 0
    k = len(dataMat) / number
    if k > 0:
        while len(sample) != number:
            sample.append(dataMat[0 + i * k])
            i += 1
        return sample
    else:
        return RandomSampling(dataMat, number)


# 分层抽样
def StratifiesSampling(dataMat1, dataMat2, dataMat3, number):
    sample = []
    num = number / 3
    sample.append(RandomSampling(dataMat1, num))
    sample.append(RandomSampling(dataMat2, num))
    sample.append(RandomSampling(dataMat3, num))
    return sample
