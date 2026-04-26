import os

INPUT_FILE = r"D:\Users\H1594\Desktop\corpus_clean_100k.txt"
OUTPUT_FILE = r"D:\Users\H1594\Desktop\corpus_char_segmented.txt"

def char_segment(input_path, output_path):
    print("正在进行中文字级拆分...")
    with open(input_path, 'r', encoding='utf-8') as f_in, \
         open(output_path, 'w', encoding='utf-8') as f_out:
        for line in f_in:
            line = line.strip()
            if not line: continue
            # 方案 B 的核心：直接 list(string) 得到字列表，再用空格拼接
            chars = [c for c in list(line) if c.strip()]
            f_out.write(" ".join(chars) + "\n")

if __name__ == "__main__":
    char_segment(INPUT_FILE, OUTPUT_FILE)
    print("字级拆分完成！")