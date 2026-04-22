import csv
from snownlp import SnowNLP

def get_sentiment(text):
    """情感分析函数：返回情感分数（0~1）和情感标签"""
    # 使用SnowNLP进行情感分析，分数越接近1越正面，越接近0越负面
    s = SnowNLP(text)
    sentiment_score = s.sentiments

    # 根据分数判断情感标签
    if sentiment_score > 0.7:
        label = "正面"
    elif sentiment_score < 0.3:
        label = "负面"
    else:
        label = "中性"

    # 保留3位小数，便于后续分析
    return round(sentiment_score, 3), label

input_file = 'clean_comment.csv'
out_file = 'final_comment.csv'

with open(input_file,'r',encoding='utf-8-sig') as f_in,\
    open(out_file,'w',encoding='utf-8-sig') as f:

        reader = csv.DictReader(f_in)
        writer = csv.writer(f)
        writer.writerow(['用户名','原评论','预处理后评论','情感分数','label'])
        count = 0

        for row in reader:
            username = row.get('用户名', "")
            original = row.get('原评论',"")
            clean_comment = row.get('预处理后评论',"")

            score,label = get_sentiment(row.get('预处理后评论'))

            writer.writerow([username, original , clean_comment , score, label])

            count+=1

print('完成')
print(f"共标记{count}条数据")

