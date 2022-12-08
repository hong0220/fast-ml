# -*- coding: UTF-8 -*-

from sklearn.datasets import load_digits
# 多层感知器
from sklearn.neural_network import MLPClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# 数据生成
data = load_digits()
X = data.images.reshape(len(data.images), -1)
y = data.target

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3)
model = MLPClassifier(hidden_layer_sizes=(16,))

# 训练
model.fit(X_train, y_train)

# 评估
y_pred = model.predict(X_test)
print(accuracy_score(y_pred, y_test))
