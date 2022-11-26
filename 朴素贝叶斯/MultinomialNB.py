# -*- coding: UTF-8 -*-

from sklearn.naive_bayes import MultinomialNB

# 数据生成
X_train = [[1, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0],
           [0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0],
           [1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0],
           [0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 1]]
y_train = [1, 1, 1, 0, 0, 0]

# 多项式朴素贝叶斯
model = MultinomialNB()

model.fit(X_train, y_train)

y_pred = model.predict([[1, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0]])
print(y_pred)
