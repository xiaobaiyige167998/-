import requests
from bs4 import BeautifulSoup
from concurrent.futures import ThreadPoolExecutor
import csv

# 请求
def get_url(url):
    try:
        resp = requests.get(url)
        resp.encoding='utf-8'
        print(f'正在打印 {url}')
        return get_html(resp.text)
    except Exception as e:
        print(f"❌ 请求失败: {url}, 错误: {str(e)}")
        return None

# 解析
def get_html(html):
    data = BeautifulSoup(html, 'html.parser')
    text = data.find_all('li', attrs={'class': 'col-xs-6 col-sm-4 col-md-3 col-lg-3'})
    return get_name(text)

# 获取name
def get_name(text):
    name_list = []
    for i in text:
        name = i.find('h3').find('a').get_text()
        name_list.append(name)
    return   writer_name(name_list)

# 主程序
def main():
    with ThreadPoolExecutor(50) as Th:
        for page_nums in range(1,51):
            url = f'https://books.toscrape.com/catalogue/page-{page_nums}.html'
            Th.submit(get_url,url=url)

    return None

if __name__ == '__main__':
    with open('线程池实战3.csv', 'w', encoding='utf-8') as f:
        # 写入name
        def writer_name(name_list):
            for name in name_list:
                csv_writer = csv.writer(f)
                csv_writer.writerow([name])

        main()