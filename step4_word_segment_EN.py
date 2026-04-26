import os

# 配置路径
INPUT_FILE = r"D:\Users\H1594\Desktop\en_corpus_100k.txt" # 或者是你之前 step2/3 生成的英文版
OUTPUT_FILE = r"D:\Users\H1594\Desktop\en_corpus_segmented.txt"

def segment_en_corpus(input_path, output_path):
    print("正在进行英文分词与预处理...")
    
    with open(input_path, 'r', encoding='utf-8', errors='ignore') as f_in, \
         open(output_path, 'w', encoding='utf-8') as f_out:
        
        line_idx = 0
        for line in f_in:
            # 1. 转小写并按空格切分
            words = line.lower().split()
            
            # 2. 过滤逻辑：只保留纯字母词汇，且长度大于 1（去掉 'a', 'i' 等单字或数字）
            result = [w for w in words if w.isalpha() and len(w) > 1]
            
            if result:
                # 写入文件，词与词之间用空格隔开
                f_out.write(" ".join(result) + "\n")
            
            line_idx += 1
            if line_idx % 10000 == 0:
                print(f"已处理 {line_idx} 行...")

if __name__ == "__main__":
    if os.path.exists(INPUT_FILE):
        segment_en_corpus(INPUT_FILE, OUTPUT_FILE)
        print("英文分词完成！")
    else:
        print("未找到输入文件，请检查路径。")