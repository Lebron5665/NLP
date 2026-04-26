import numpy as np
from gensim.models import Word2Vec
from sklearn.metrics.pairwise import cosine_similarity

# 加载方案 A (词级) 和 方案 B (字级)
model_a = Word2Vec.load(r"D:\Users\H1594\Desktop\zh_wiki_word2vec.model")
model_b = Word2Vec.load(r"D:\Users\H1594\Desktop\zh_char_word2vec.model")

def check_semantic_boundary(target_word):
    print(f"\n分析目标: 【{target_word}】")
    
    # 1. 获取方案 A 的整体表示
    if target_word in model_a.wv:
        v_word = model_a.wv[target_word].reshape(1, -1)
    else:
        print("词级模型中不存在该词")
        return

    # 2. 获取方案 B 的字级合成表示
    chars = [c for c in list(target_word) if c in model_b.wv]
    if not chars:
        return
    
    char_vectors = [model_b.wv[c] for c in chars]
    v_comp = np.mean(char_vectors, axis=0).reshape(1, -1)
    
    # 3. 计算余弦相似度
    sim = cosine_similarity(v_word, v_comp)[0][0]
    print(f"语义边界保持度 (余弦相似度): {sim:.4f}")
    
    # 4. 观察邻域偏离
    print(f"方案 A 近邻: {model_a.wv.most_similar(target_word, topn=3)}")
    print(f"方案 B (合成向量) 近邻: {model_b.wv.most_similar(v_comp, topn=3)}")

# 测试
check_semantic_boundary("人工智能")
check_semantic_boundary("数学")