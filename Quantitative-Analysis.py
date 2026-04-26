import matplotlib.pyplot as plt
from gensim.models import Word2Vec, FastText

# 设置中文显示
plt.rcParams['font.sans-serif'] = ['SimHei'] 

# 加载三个模型
print("正在加载模型进行定量分析...")
model_a = Word2Vec.load(r"D:\Users\H1594\Desktop\zh_wiki_word2vec.model")
model_b = Word2Vec.load(r"D:\Users\H1594\Desktop\zh_char_word2vec.model")
model_c = FastText.load(r"D:\Users\H1594\Desktop\zh_fasttext.model")

# 定义一组测试集（包含生僻词、合成词、错别字）
test_words = [
    "深度学习架构师", "非欧几里得几何", "生成式对抗网络", 
    "大语言模型", "多模态融合", "强化学习算法", 
    "Transformer模型", "量子计算架构", "分布式存储系统", "卷积神经网络"
]

def calculate_oov_rate(model, words, is_char=False):
    found = 0
    for word in words:
        if is_char:
            # 方案 B 只要第一个字在词表就算识别（因为它是按字存的）
            if word[0] in model.wv: found += 1
        else:
            if word in model.wv: found += 1
    return (found / len(words)) * 100

# 计算覆盖率
rate_a = calculate_oov_rate(model_a, test_words)
rate_b = calculate_oov_rate(model_b, test_words, is_char=True)
rate_c = calculate_oov_rate(model_c, test_words) # FastText 会自动处理 OOV

# 绘图
schemes = ['方案 A (词级)', '方案 B (字级)', '方案 C (FastText)']
rates = [rate_a, rate_b, rate_c]

plt.figure(figsize=(8, 6))
bars = plt.bar(schemes, rates, color=['#ff9999','#66b3ff','#99ff99'])
plt.ylabel('OOV 覆盖率 (%)')
plt.title('不同分词方案对生僻词/合成词的覆盖率定量对比')
plt.ylim(0, 110)

# 添加数值标签
for bar in bars:
    yval = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2, yval + 2, f'{yval}%', ha='center', va='bottom')

plt.show()