# -*- coding: UTF-8 -*-

from sklearn.datasets import load_wine
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# 数据生成
data = load_wine()

X_train, X_test, y_train, y_test = train_test_split(data.data, data.target, test_size=0.3)

model = RandomForestClassifier()

# 训练
model.fit(X_train, y_train)

# 对葡萄酒进行分类
y_pred = model.predict(X_test)

# 评估
print(accuracy_score(y_pred, y_test))
