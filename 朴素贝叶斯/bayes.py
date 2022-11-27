# -*- coding: UTF-8 -*-
# python2

from naiveBayesClassifier import tokenizer
from naiveBayesClassifier.trainer import Trainer
from naiveBayesClassifier.classifier import Classifier

newsSet = [
    {'text': 'not to eat too much is not enough to lose weight', 'category': 'health'},
    {'text': 'Russia try to invade Ukraine', 'category': 'politics'},
    {'text': 'do not neglect exercise', 'category': 'health'},
    {'text': 'Syria is the main issue, Obama says', 'category': 'politics'},
    {'text': 'eat to lose weight', 'category': 'health'},
    {'text': 'you should not eat much', 'category': 'health'}
]
# 分类模型
newsTrainer = Trainer(tokenizer)
for news in newsSet:
    # 训练分类模型
    newsTrainer.train(news['text'], news['category'])

# 每个词在不同种类的训练样本中出现概率大小,类别:health,politics
newsClassifier = Classifier(newsTrainer.data, tokenizer)

classification = newsClassifier.classify("eat more, you will become fatter")
print(classification)
