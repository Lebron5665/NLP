from gensim.models import Word2Vec
import os

# 1. 配置路径
INPUT_FILE = r"D:\Users\H1594\Desktop\en_corpus_segmented.txt"
MODEL_PATH = r"D:\Users\H1594\Desktop\en_wiki_word2vec.model"

def train_en_model():
    print("加载英文分词语料...")
    sentences = []
    
    if not os.path.exists(INPUT_FILE):
        print("错误：找不到分词后的英文语料文件！")
        return

    with open(INPUT_FILE, 'r', encoding='utf-8') as f:
        for line in f:
            sentences.append(line.split())

    # 2. 初始化并训练模型
    print(f"开始训练英文模型，共 {len(sentences)} 条句子...")
    model = Word2Vec(
        sentences=sentences, 
        vector_size=200, 
        window=5, 
        min_count=5, 
        workers=4, 
        sg=1  # 依然推荐使用 Skip-gram
    )

    # 3. 保存模型
    model.save(MODEL_PATH)
    print(f"英文模型训练完成，保存至: {MODEL_PATH}")

if __name__ == "__main__":
    train_en_model()