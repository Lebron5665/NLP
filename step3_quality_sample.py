import re
import os
import random

INPUT_FILE = r"D:\Users\H1594\Desktop\zh_corpus.txt"
OUTPUT_FILE = r"D:\Users\H1594\Desktop\corpus_clean_100k.txt"
MAX_LINES = 100000

def is_good_sentence(text):
    # 进一步收紧过滤网
    noise = ["category:", "image:", "file:", "uploaded", "已删除", "存档", "上载", "参见", "外部链接"]
    if any(k in text.lower() for k in noise): return False
    
    # 统计汉字数，真正的百科句子通常较长且含有标点
    zh_chars = re.findall(r'[\u4e00-\u9fa5]', text)
    if len(zh_chars) < 15:  # 长度少于15个汉字的短语通常是词典定义，过滤掉
        return False
    return True

def clean_tags(text):
    text = re.sub(r'\[\[(?:[^|\]]*\|)?([^\]]+)\]\]', r'\1', text) # 处理链接
    text = re.sub(r'\{{.*?\}}', '', text) # 处理模板
    return text.strip()

def fast_sample(input_path, output_path, max_lines):
    print("正在启动随机跳跃模式，寻找高质量百科正文...")
    line_count = 0
    file_size = os.path.getsize(input_path)
    
    with open(input_path, 'r', encoding='utf-8', errors='ignore') as f_in, \
         open(output_path, 'w', encoding='utf-8') as f_out:
        
        while line_count < max_lines:
            # 随机跳到文件的一个位置
            f_in.seek(random.randint(0, file_size - 1000))
            f_in.readline() # 舍弃掉可能切断的第一行
            
            # 读取接下来的 50 行寻找黄金句子
            for _ in range(50):
                line = f_in.readline()
                if not line: break
                
                # 按照标点切分
                sentences = re.split(r'([。！？])', line)
                for i in range(0, len(sentences)-1, 2):
                    s = (sentences[i] + sentences[i+1]).strip()
                    s = clean_tags(s)
                    
                    if is_good_sentence(s):
                        f_out.write(s + "\n")
                        line_count += 1
                    
                    if line_count >= max_lines:
                        print(f"提取完成！已抓取 {line_count} 行高质量正文。")
                        return
            
            if line_count % 5000 == 0:
                print(f"已收集 {line_count} 条高质量句子...")

if __name__ == "__main__":
    if os.path.exists(INPUT_FILE):
        fast_sample(INPUT_FILE, OUTPUT_FILE, MAX_LINES)
    else:
        print("未找到输入文件。")