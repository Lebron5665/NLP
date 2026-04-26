from gensim.models import Word2Vec
import os

# 1. 读取方案 B 生成的字级语料
INPUT_FILE = r"D:\Users\H1594\Desktop\corpus_char_segmented.txt"
MODEL_PATH = r"D:\Users\H1594\Desktop\zh_char_word2vec.model"

def train_char_model():
    if not os.path.exists(INPUT_FILE):
        print("错误：请先运行 step4_char_segment.py 生成字级语料！")
        return

    sentences = []
    print("加载字级语料中...")
    with open(INPUT_FILE, 'r', encoding='utf-8') as f:
        for line in f:
            sentences.append(line.split())

    print("开始训练方案 B：字级 Word2Vec 模型...")
    model = Word2Vec(
        sentences=sentences, 
        vector_size=200, 
        window=5, 
        min_count=5, 
        sg=1
    )
    model.save(MODEL_PATH)
    print(f"方案 B 训练完成！保存至：{MODEL_PATH}")

if __name__ == "__main__":
    train_char_model()