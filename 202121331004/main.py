import gensim.corpora
import jieba
from math import sqrt
import re

from gensim import corpora


# 根据读入的文件路径读取文件,对文章进行分词并将标点符号过滤
def deal_file(path):
    ans = ""
    with open(path, encoding='utf-8') as file:
        line = file.readline()
        while line != '':
            ans = ans + line
            line = file.readline()
    file.close()
    # 分词
    s = jieba.cut(s)
    ans = []
    # 通过正则表达式过滤标点符号
    for i in s:
        if re.match(u"[a-zA-Z0-9\u4e00-\u9fa5]", i) is not None:
            ans.append(i)
        else:
            pass
    return ans

# 构造向量并计算余弦相似度
def cosine_similarity(t1, t2):
    # 构造向量
    txt = [t1, t2]
    dict = gensim.corpora.Dictionary(txt)
    corp = [dict.doc2bow(t) for t in txt]
    # 计算余弦相似度
    sim = gensim.similarities.Similarity('-Similarity-index', corp, num_features = len(dict))
    corp1 = dict.doc2bow(t1)
    return sim[corp1][1]
