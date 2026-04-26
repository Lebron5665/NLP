import jieba
import os

# 配置路径
INPUT_FILE = r"D:\Users\H1594\Desktop\corpus_clean_100k.txt"
OUTPUT_FILE = r"D:\Users\H1594\Desktop\corpus_segmented.txt"

def segment_corpus(input_path, output_path):
    print("正在进行中文分词...")
    
    # 如果你有停用词表，可以在这里加载
    # stop_words = set([...]) 
    
    with open(input_path, 'r', encoding='utf-8') as f_in, \
         open(output_path, 'w', encoding='utf-8') as f_out:
        
        line_idx = 0
        for line in f_in:
            line = line.strip()
            if not line:
                continue
                
            # 使用 jieba 精确模式分词
            words = jieba.cut(line)
            
            # 过滤掉单字和纯标点（可选，有助于提升词向量质量）
            result = [w for w in words if len(w) > 1]
            
            if result:
                # Word2Vec 要求的格式：词与词之间用空格隔开
                f_out.write(" ".join(result) + "\n")
            
            line_idx += 1
            if line_idx % 10000 == 0:
                print(f"已处理 {line_idx} 行...")

if __name__ == "__main__":
    segment_corpus(INPUT_FILE, OUTPUT_FILE)
    print(f"分词完成！请检查生成的文件：{OUTPUT_FILE}")