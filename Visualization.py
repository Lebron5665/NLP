import matplotlib.pyplot as plt
from sklearn.manifold import TSNE
import numpy as np
from gensim.models import Word2Vec

# 设置中文字体（防止乱码）
plt.rcParams['font.sans-serif'] = ['SimHei'] 

def plot_nodes(model, words):
    embeddings = np.array([model.wv[w] for w in words if w in model.wv])
    labels = [w for w in words if w in model.wv]
    
    # 使用 t-SNE 降维到 2 维
    tsne = TSNE(n_components=2, perplexity=5, init='pca', random_state=42)
    low_dim_embs = tsne.fit_transform(embeddings)
    
    plt.figure(figsize=(10, 8))
    for i, label in enumerate(labels):
        x, y = low_dim_embs[i, :]
        plt.scatter(x, y)
        plt.annotate(label, xy=(x, y), xytext=(5, 2), textcoords='offset points')
    plt.title("科学领域词汇语义空间分布 (方案 A)")
    plt.show()

# 测试词簇
science_words = ['数学', '物理学', '微积分', '代数', '几何', '软件工程', '人工智能', '算法', '数据库']
model = Word2Vec.load(r"D:\Users\H1594\Desktop\zh_wiki_word2vec.model")
plot_nodes(model, science_words)