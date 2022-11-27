# -*- coding: UTF-8 -*-

from sklearn.linear_model import LinearRegression

# from sklearn import linear_model

# 两个特征
X = [[5, 2], [2, 5], [3, 9]]
y = [0, 1, 2]

model = LinearRegression()
model.fit(X, y)

# 截距
print(model.intercept_)
# 斜率
print(model.coef_)

# 预测
y_pred = model.predict([[1, 1], [3, 3]])
print(y_pred)
