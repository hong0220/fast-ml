# -*- coding: UTF-8 -*-

from sklearn.naive_bayes import GaussianNB

# 数据生成
X_train = [[1, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0],
           [0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0],
           [1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0],
           [0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 1]]
y_train = [1, 1, 1, 0, 0, 0]

# 高斯朴素贝叶斯
model = GaussianNB()

model.fit(X_train, y_train)

y_pred = model.predict([[1, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0]])
print(y_pred)
