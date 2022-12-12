# -*- coding: UTF-8 -*-

import random

# 一个用户的标签行为一般由一个三元组组成<用户,物品,标签>(<u,i,b>)即用户u给物品i打上了b标签。
# 1.统计每个用户最常用标签；
# 2.对于每个标签,统计被打过这个标签次数最多的物品；
# 3.对于一个用户,找到他常用的标签,从而找到具有这些标签的热门物品进行推荐。

# 存储用户u打过标签b的次数,即 userLabels[u][b]
userLabels = dict()

# 存储物品i被打过标签b的次数,即 labelItems[b][i]
labelItems = dict()

# 存储用户所打过标签的物品,即 userItems[u][i]
userItems = dict()

# 测试集数据字典
userItemsTest = dict()


# 初始化,进行各种统计
def InitStat():
    dataFile = open('xxx.dat')
    line = dataFile.readline()
    while line:
        # 将90%的数据作为训练集,剩下10%的数据作为测试集
        if random.random() > 0.1:
            # 训练集的数据结构是[user,item,label]形式
            terms = line.split(",")
            user = terms[0]
            item = terms[1]
            label = terms[2]
            addValueToMat(userLabels, user, label, 1)
            addValueToMat(labelItems, label, item, 1)
            addValueToMat(userItems, user, item, 1)

            line = dataFile.readline()
        else:
            addValueToMat(userItemsTest, user, item, 1)
    dataFile.close()


# 统计各类数量
def addValueToMat(mat, key, value, incr):
    # 如果key没在theMat中
    if key not in mat:
        mat[key] = dict()
        mat[key][value] = incr
    else:
        if value not in mat[key]:
            mat[key][value] = incr
        else:
            # 若有值,则累加
            mat[key][value] += incr


# 推荐算法
def recommend(usr):
    # 得到用户所有推荐过的物品
    recommendList = dict()

    # 得到用户打过的标签和次数
    for tag, wut in userLabels[usr].items():
        # 物品被打过的标签和被打过的次数
        for item, wit in labelItems[tag].items():
            # 得到用户所有推荐过的物品,已经推荐推荐过不再
            if item not in userItems[usr]:
                if item not in recommendList:
                    # 根据公式
                    recommendList[item] = wut * wit
                else:
                    # 根据公式
                    recommendList[item] += wut * wit

    return recommendList
