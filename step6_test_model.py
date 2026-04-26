from gensim.models import Word2Vec

# 加载你刚训好的模型
model = Word2Vec.load(r"D:\Users\H1594\Desktop\zh_wiki_word2vec.model")

# 看看和“数学”最像的词
print("与‘数学’最接近的词：")
print(model.wv.most_similar("数学", topn=5))

# 看看和“人工智能”最像的词
print("\n与‘人工智能’最接近的词：")
print(model.wv.most_similar("人工智能", topn=5))