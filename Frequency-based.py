from gensim.models import Word2Vec, FastText

# 加载模型
model_a = Word2Vec.load(r"D:\Users\H1594\Desktop\zh_wiki_word2vec.model")
model_c = FastText.load(r"D:\Users\H1594\Desktop\zh_fasttext.model")

def analyze_frequency_degradation(word):
    print(f"\n测试词汇: 【{word}】")
    
    # 方案 A 结果
    try:
        sims_a = model_a.wv.most_similar(word, topn=3)
        print(f"方案 A (Word2Vec) 近邻: {sims_a}")
    except KeyError:
        print(f"方案 A: 词汇不存在 (OOV)")

    # 方案 C 结果
    try:
        sims_c = model_c.wv.most_similar(word, topn=3)
        print(f"方案 C (FastText) 近邻: {sims_c}")
    except Exception as e:
        print(f"方案 C 报错: {e}")

# 1. 测试高频词
print("--- 高频词测试 ---")
analyze_frequency_degradation("数学")

# 2. 测试低频专业词（请确保语料中包含这些字，否则用你语料里的低频专业词替换）
print("\n--- 低频词测试 ---")
analyze_frequency_degradation("黎曼流形")