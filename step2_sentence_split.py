import re
import os

# 配置路径
#INPUT_FILE = r"D:\Users\H1594\Desktop\en_corpus.txt" 
#OUTPUT_FILE = r"D:\Users\H1594\Desktop\en_corpus_100k.txt"
INPUT_FILE = r"D:\Users\H1594\Desktop\zh_corpus.txt" 
OUTPUT_FILE = r"D:\Users\H1594\Desktop\zh_corpus_100k.txt"
MAX_LINES = 100000

def format_wiki_text(input_path, output_path, max_lines):
    print(f"正在处理: {input_path}")
    line_count = 0
    
    # 匹配句子结束符号的正则（中英文通用）
    sentence_splitter = re.compile(r'([。！？.!?])')
    
    # 清洗维基标签的正则
    wiki_tag_re = re.compile(r'(thumb|right|left|upright|px|\||\[\[|\]\])')

    with open(input_path, 'r', encoding='utf-8', errors='ignore') as f_in, \
         open(output_path, 'w', encoding='utf-8') as f_out:
        
        for raw_line in f_in:
            if line_count >= max_lines:
                break
            
            # 1. 初步清洗噪音
            clean_text = wiki_tag_re.sub('', raw_line)
            
            # 2. 核心操作：通过正则在标点符号后切分，变“单行”为“多行”
            # split后会变成 ['句子1', '.', '句子2', '!', '']
            parts = sentence_splitter.split(clean_text)
            
            # 重新组合句子和标点
            current_sentence = ""
            for i in range(0, len(parts)-1, 2):
                sentence = (parts[i] + parts[i+1]).strip()
                
                # 过滤掉太短的碎片（小于10个字符通常是无意义的）
                if len(sentence) > 10:
                    f_out.write(sentence + '\n')
                    line_count += 1
                
                # 达到10万行立即退出内循环
                if line_count >= max_lines:
                    break
                    
            if line_count % 5000 == 0:
                print(f"已提取 {line_count} 行...")

    print(f"处理完成！最终生成文件: {output_path}")
    print(f"当前文件行数: {line_count}")

if __name__ == "__main__":
    format_wiki_text(INPUT_FILE, OUTPUT_FILE, MAX_LINES)