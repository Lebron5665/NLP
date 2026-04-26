from gensim.models import Word2Vec

# 加载英文模型
MODEL_PATH = r"D:\Users\H1594\Desktop\en_wiki_word2vec.model"
model = Word2Vec.load(MODEL_PATH)

def test_word(word):
    try:
        print(f"\n与 '{word}' 最接近的英文词：")
        results = model.wv.most_similar(word, topn=5)
        for res in results:
            print(f"{res[0]}: {res[1]:.4f}")
    except KeyError:
        print(f"词汇 '{word}' 不在词典中。")

if __name__ == "__main__":
    test_word("mathematics")
    test_word("computer")
    test_word("ai")