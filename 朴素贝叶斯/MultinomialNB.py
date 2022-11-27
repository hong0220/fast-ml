# -*- coding: UTF-8 -*-

from sklearn.naive_bayes import MultinomialNB

# Bow文本表示方式生成数据
X_train = [[1, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0],
           [0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0],
           [1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0],
           [0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 1]]
y_train = [1, 1, 1, 0, 0, 0]

# 多项式朴素贝叶斯
model = MultinomialNB()

# 训练
model.fit(X_train, y_train)

# 评估，预测新闻标题
y_pred = model.predict([[1, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0]])
print(y_pred)
