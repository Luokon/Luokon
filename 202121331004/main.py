import gensim.corpora
import jieba
import re

# 根据读入的文件路径读取文件,对文章进行分词并将标点符号过滤
def deal_file(path):
    s = ""
    with open(path, encoding='utf-8') as f:
        line = f.readline()
        while line != '':
            s = s + line
            line = f.readline()
    f.close()
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
    dictionary = gensim.corpora.Dictionary(txt)
    vec = [dictionary.doc2bow(t) for t in txt]
    # 计算余弦相似度
    sim = gensim.similarities.Similarity('-Similarity-index', vec, num_features = len(dictionary))
    corp1 = dictionary.doc2bow(t1)
    return sim[corp1][1]

if __name__ == '__main__' :
    print("请输入原论文的文件路径：")
    path1 = input()
    print("请输入抄袭论文的文件路径")
    path2 = input()

    # path1 = "F:\\py_code\\Luokon\\202121331004\\test\\orig.txt"
    # path2 = "F:\\py_code\\Luokon\\202121331004\\test\\orig.add.txt"
    res_path = "F:\\py_code\\Luokon\\202121331004\\test\\res.txt"

    # 处理文章，返回过滤符号并分词的列表
    txt1 = deal_file(path1)
    txt2 = deal_file(path2)

    # 计算余弦相似度并写入结果文件
    ans = cosine_similarity(txt1, txt2)
    print("两篇文章的相似度：%.2f" %ans)
    file = open(res_path, 'w', encoding='utf-8')
    file.write("两篇文章的相似度：%.2f" %ans)
    file.close()