# -*- coding: UTF-8 -*-

from sklearn import datasets
from sklearn.semi_supervised import LabelPropagation
import numpy as np

label_prop_model = LabelPropagation()

# 数据源，4个特征，label:0,1,2
iris = datasets.load_iris()
print(iris)

# 生成半监督数据
# 范围:0,1 size:长度
array = np.random.randint(0, 2, size=len(iris.target))
print(array)
# where:1的索引位置
random_unlabeled_points = np.where(array)
print(random_unlabeled_points)
labels = np.copy(iris.target)
# 目标列为-1
labels[random_unlabeled_points] = -1

# 训练模型并预测
label_prop_model.fit(iris.data, labels)

# 评估
index = 0
for i in range(0, len(iris['target'])):
    if (iris['target'][i]) == (label_prop_model.predict(iris.data)[i]):
        index = index + 1
print('The right number of prediction:' + str(index))
print('The total number of dataset:' + str(len(iris['target'])))
