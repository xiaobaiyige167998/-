import requests
from lxml import etree
from concurrent.futures import ThreadPoolExecutor,ProcessPoolExecutor
import csv

# 1.先获取单页的数据
# 2.后通过线程池进行爬取


f = open('线程池实战.csv','w',encoding='utf-8')
cavwriter = csv.writer(f)    #给文件 f 创建一个CSV 写入工具，这个工具会帮你按 CSV 格式规范地写数据。 并赋值给变量cavwriter

def get_url(url):
    resp = requests.get(url)
    resp.encoding = 'utf-8'
    Html = etree.HTML(resp.text)
    data = Html.xpath('//ol[@class="row"]/li')
    for i in data:
       name = i.xpath('.//h3/a/text()')
       cavwriter.writerow(name)   # csvwriter = 你创建的CSV 写字工具，即变量。   writerow为写一行数据
    print(url,'提取完毕！')



if __name__ == '__main__':
    with ThreadPoolExecutor(50) as p:
        for m in range(1,50):
            url = f'https://books.toscrape.com/catalogue/page-{m}.html'
            p.submit(get_url,url=url)









