from gensim.models import Word2Vec, FastText
import os

# 配置模型路径
path_a = r"D:\Users\H1594\Desktop\zh_wiki_word2vec.model"
path_b = r"D:\Users\H1594\Desktop\zh_char_word2vec.model"
path_c = r"D:\Users\H1594\Desktop\zh_fasttext.model"

print("正在加载三大方案模型进行巅峰对决...")
model_a = Word2Vec.load(path_a)
model_b = Word2Vec.load(path_b)
model_c = FastText.load(path_c)

def final_compare(word):
    print(f"\n" + "="*30)
    print(f"测试词汇: 【{word}】")
    
    # 方案 A: 词级 Word2Vec
    try:
        sim = model_a.wv.most_similar(word, topn=1)
        print(f"方案 A (词级W2V): 已识别 | 最相似: {sim[0][0]} ({sim[0][1]:.3f})")
    except:
        print(f"方案 A (词级W2V): ❌ 报错！触发 OOV (无法识别该词)")

    # 方案 B: 字级 Word2Vec
    char_to_test = word[0] if len(word)>0 else ""
    try:
        sim = model_b.wv.most_similar(char_to_test, topn=1)
        print(f"方案 B (字级W2V): 识别单字【{char_to_test}】 | 最相似: {sim[0][0]} ({sim[0][1]:.3f})")
    except:
        print(f"方案 B (字级W2V): ❌ 无法识别该字")

    # 方案 C: FastText (子词级)
    try:
        sim = model_c.wv.most_similar(word, topn=1)
        print(f"方案 C (FastText): 完美识别 | 最相似: {sim[0][0]} ({sim[0][1]:.3f})")
    except:
        print(f"方案 C (FastText): ❌ 报错")

if __name__ == "__main__":
    # 1. 词典内词汇
    final_compare("数学")
    # 2. 词典外词汇 (OOV 测试)
    final_compare("深度学习架构师")
    # 3. 英文词汇
    final_compare("pysics")