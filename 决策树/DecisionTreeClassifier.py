# -*- coding: UTF-8 -*-

from sklearn import tree

# gini or entropy (information gain)
model = tree.DecisionTreeClassifier(criterion='gini')

model.fit(X, y)
model.score(X, y)

predicted = model.predict(x_test)
print(predicted)