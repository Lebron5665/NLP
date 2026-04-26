import bz2
import xml.etree.ElementTree as ET
import mwparserfromhell
from opencc import OpenCC
from tqdm import tqdm
import re

def process_wiki(input_file, output_file, lang='zh', limit=50000):
    print(f"开始处理 {input_file}...")
    cc = OpenCC('t2s') if lang == 'zh' else None
    count = 0
    
    # 预编译正则，提升效率
    tag_re = re.compile(r'<.*?>')
    
    with bz2.open(input_file, 'rb') as f_in, open(output_file, 'w', encoding='utf-8') as f_out:
        # 使用 iterparse 流式读取
        context = ET.iterparse(f_in, events=('end',))
        
        pbar = tqdm(total=limit, desc=f"Extracting {lang}")
        for event, elem in context:
            # 只要 <text> 标签里的内容
            if elem.tag.endswith('text'):
                text = elem.text
                if text:
                    # 1. 使用 mwparserfromhell 去除维基语法（表格、链接、模板）
                    parsed_text = mwparserfromhell.parse(text).strip_code()
                    
                    # 2. 基本清洗：去除剩余的 HTML 标签
                    clean_text = tag_re.sub('', parsed_text)
                    
                    # 3. 针对中文进行繁简转换
                    if cc:
                        clean_text = cc.convert(clean_text)
                    
                    # 4. 格式化：去除多余换行，确保每篇文章占一行（或一段）
                    final_text = " ".join(clean_text.split())
                    
                    if len(final_text) > 50: # 过滤掉太短的废话
                        f_out.write(final_text + '\n')
                        count += 1
                        pbar.update(1)
                
                # 显式清理内存中的元素，防止 OOM
                elem.clear()
            
            if count >= limit:
                break
        pbar.close()

if __name__ == "__main__":
    # ================= 修改后的路径区域 =================
    # 输入文件路径
    zh_input = r"D:\Users\H1594\Desktop\zhwiki-latest-pages-articles.xml.bz2"
    en_input = r"D:\Users\H1594\Desktop\enwiki-latest-pages-articles.xml.bz2"
    
    # 输出文件路径（也指向桌面）
    zh_output = r"D:\Users\H1594\Desktop\zh_corpus.txt"
    en_output = r"D:\Users\H1594\Desktop\en_corpus.txt"

    # 处理中文（如果有文件则取消下面一行的注释）
    process_wiki(zh_input, zh_output, lang='zh', limit=50000)
    
    # 处理英文
    process_wiki(en_input, en_output, lang='en', limit=50000)
    # ==================================================

    print(f"\n第一阶段完成！文件已保存在: D:\\Users\\H1594\\Desktop\\")