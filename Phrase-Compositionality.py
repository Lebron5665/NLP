from gensim.models import Word2Vec

model_a = Word2Vec.load(r"D:\Users\H1594\Desktop\zh_wiki_word2vec.model")

print("--- 4.3 组合词可组合性测试 ---")

# 测试 1: 语义偏移 (人工智能 - 算法 + 硬件)
print("\n测试 1: 人工智能 - 算法 + 硬件")
res1 = model_a.wv.most_similar(positive=['人工智能', '硬件'], negative=['算法'], topn=3)
for word, sim in res1:
    print(f"预测结果: {word}, 相似度: {sim:.4f}")

# 测试 2: 语义加和 (数学 + 物理)
print("\n测试 2: 数学 + 物理 (语义加和)")
res2 = model_a.wv.most_similar(positive=['数学', '物理'], topn=3)
for word, sim in res2:
    print(f"预测结果: {word}, 相似度: {sim:.4f}")