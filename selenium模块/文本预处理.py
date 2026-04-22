import re
import csv

def clean_text(text):
    """文本预处理函数：清洗评论内容，去除无效信息"""
    if not text:
        return ""

    # 1. 去除首尾空格、换行符
    text = text.strip()

    # 2. 去除网址（http/https/www开头的链接）
    text = re.sub(r'http\S+|www.\S+', '', text)

    # 3. 去除@用户、话题标签（#XXX#）
    text = re.sub(r'@\w+|#\w+#', '', text)

    # 4. 只保留中文、英文、数字和常用标点，去除特殊符号
    text = re.sub(r'[^\u4e00-\u9fa5a-zA-Z0-9，。！？；：""'',.!?;: ]', '', text)

    # 5. 多个空格合并为一个
    text = re.sub(r'\s+', ' ', text)

    return text


input_file='edge_comments.csv'
output = 'clean_comment.csv'

with open(input_file,'r',encoding='utf-8-sig') as f_in,\
        open(output,'w',newline='',encoding='utf-8-sig') as f_out:

    reader=csv.DictReader(f_in)
    writer=csv.writer(f_out)

    writer.writerow(['用户名','原评论','预处理后评论'])

    count = 0

    for row in reader:
        username = row.get('用户名',"")
        content = row.get('评论内容',"")
        clean_content = clean_text(content)


        if len(clean_content)<2:
            continue

        writer.writerow([username,content,clean_content])

        count+=1

print('完成')
print(f'有效数据：{count}条')



















