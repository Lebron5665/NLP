from gensim.models import Word2Vec

# 1. 读取你刚才分好词的文件
sentences = []
with open(r"D:\Users\H1594\Desktop\corpus_segmented.txt", 'r', encoding='utf-8') as f:
    for line in f:
        sentences.append(line.split()) # 将每一行转为词列表

# 2. 初始化并训练模型
print("模型训练中...")
model = Word2Vec(
    sentences=sentences, 
    vector_size=200,  # 词向量维度，通常设为 100-300
    window=5,         # 扫描的上下文窗口大小
    min_count=5,      # 过滤掉出现次数少于 5 次的生僻词
    workers=4,        # 电脑并行核心数
    sg=1              # 1 表示用 Skip-gram 算法（对专业术语效果更好）
)

# 3. 保存训练好的模型
model.save(r"D:\Users\H1594\Desktop\zh_wiki_word2vec.model")
print("训练完成，模型已保存！")