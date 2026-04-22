import csv
import matplotlib.pyplot as plt

#导入文件
input_file = 'final_comment.csv'

# 初始化
sentiment_counts = {
    "正面":0,
    "中性":0,
    "负面":0
}

with open(input_file,'r',encoding='utf-8-sig') as f:
    reader = csv.DictReader(f)
    for row in reader:
        if row.get('label') == '正面':
            sentiment_counts['正面']+=1
        elif row.get('label') == '中性':
            sentiment_counts['中性']+=1
        else:
            sentiment_counts['负面']+=1

print(sentiment_counts)

# 绘制柱状图
labels = list(sentiment_counts.keys())
plt.bar(labels, counts, color=["#FF6B6B", "#4ECDC4", "#45B7D1"])  # 三种颜色区分情感类型
plt.title("评论情感分布柱状图", fontsize=14)  # 图表标题
plt.xlabel("情感类型", fontsize=12)  # x轴标签
plt.ylabel("评论数量", fontsize=12)  # y轴标签
























