from gensim.models import FastText
import os

# 使用方案 A 的词级语料作为输入
INPUT_FILE = r"D:\Users\H1594\Desktop\corpus_segmented.txt"
MODEL_PATH = r"D:\Users\H1594\Desktop\zh_fasttext.model"

def train_fasttext():
    if not os.path.exists(INPUT_FILE):
        print("错误：请先运行 4.py 生成分词语料！")
        return

    sentences = []
    print("加载方案 A 语料进行 FastText 训练...")
    with open(INPUT_FILE, 'r', encoding='utf-8') as f:
        for line in f:
            sentences.append(line.split())

    # 训练 FastText：关键在于它会自动提取子词特征
    model = FastText(
        sentences=sentences, 
        vector_size=200, 
        window=5, 
        min_count=5, 
        sg=1,  # 使用 Skip-gram
        epochs=5
    )
    model.save(MODEL_PATH)
    print(f"方案 C 训练完成！FastText 模型已保存：{MODEL_PATH}")

if __name__ == "__main__":
    train_fasttext()