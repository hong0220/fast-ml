# -*- coding: UTF-8 -*-

from math import log


# Term Frequency
# 单词在文章出现频率
def tf(word, doc):
    all_num = sum([doc[key] for key in doc])
    return float(doc[word]) / all_num


# Document Frequency
# 出现单词的文章占所有文章的比例，求倒数，取对数
def idf(word, doc_list):
    all_num = len(doc_list)
    word_count = 0
    for doc in doc_list:
        if word in doc:
            word_count += 1
    return log(all_num / word_count)


# Term Frequency-inverse Document Frequency
# 词频-逆向文件频率
def TF_IDF(word, doc, doc_list):
    score = tf(word, doc) * idf(word, doc_list)
    return score


if __name__ == '__main__':
    doc1 = {'at': 16, 'tell': 132, 'soft': 42, 'let': 53, 'this': 32}
    doc2 = {'tell': 53, 'be': 46, 'tea': 43, 'what': 46, 'foot': 65, 'hack': 32}
    doc3 = {'soft': 65, 'this': 67, 'tell': 78, 'how': 124, 'foot': 54}

    doc_list = [doc1, doc2, doc3]
    i = 1
    for doc in doc_list:
        print('-' * 20)
        print('doc%d' % i)
        for word in doc:
            print('"%s":%f' % (word, TF_IDF(word, doc, doc_list)))
        i += 1
