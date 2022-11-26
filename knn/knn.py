# -*- coding: UTF-8 -*-

from sklearn.neighbors import KNeighborsClassifier
from sklearn.datasets import make_moons
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# 曲线分布的样本数据生成
X, y = make_moons(noise=0.3)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3)

# k 默认值为5
model = KNeighborsClassifier()

# 训练
model.fit(X_train, y_train)

y_pred = model.predict(X_test)

# 评估
print(accuracy_score(y_pred, y_test))
