import jieba
import gensim
import re

#读取文件
def readFile(path):
    ans = ''
    f = open(path, 'r', encoding='UTF-8')
    s = f.readline()
    while s :
        ans += s
        s = f.readline
    f.close()
    return s;

#对文章进行分词并将标点符号过滤
def dealFile(s):
    s = jieba.lcut(s)
    ans = []
    for i in s:
        if re.match(u"[a-zA-Z0-9\u4e00-\u9fa5]", i):
            ans.append(i)
        else: pass
    return ans

