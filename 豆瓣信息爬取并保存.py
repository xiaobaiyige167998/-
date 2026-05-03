import requests
from bs4 import BeautifulSoup
from concurrent.futures import ThreadPoolExecutor
import csv
import time
import threading

lock = threading.Lock()

def main1(url):
    headers = {
        "user-agent":
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/147.0.0.0 Safari/537.36 Edg/147.0.0.0"}

    for attempt in range(1,4):
        try:
            html = requests.get(url,headers=headers).text
            return main(html)
        except Exception as e:
            print(f'第{attempt}次失败')
            if attempt < 3:
                time.sleep(attempt * 2)  # 没到第3次就等待

def main(html):
    soup = BeautifulSoup(html, 'html.parser')
    li_list = soup.find('ol', class_='grid_view').find_all('li')

    for li in li_list:
        title = li.find('span',class_='title').text.strip()
        name = li.find('p').text.split('主演')[0].strip()

        parts = li.find('p').text.split('...')  #防止没有此内容报错
        movie_text = parts[1].strip() if len(parts) > 1 else ''

        rating_tag = li.find('span', class_='rating_num')  #防止没有此内容报错
        price = rating_tag.text.strip() if rating_tag else '暂无评分'

        pop_price = li.find('div',class_='bd').find('div').find_all('span')[-1].text.strip()

        # print(f'电影名称:{title}, 评分:{price}, 评价人数:{pop_price}, {name}, 电影信息:{movie_text}\n')
        # csv_writer.writerow([title,price,pop_price,name,movie_text])

        with lock:  # ← 加这个，写入前抢锁，写完自动释放
            csv_writer.writerow([title, price, pop_price, name, movie_text])

if __name__ == '__main__':
    with open('raw_movies.csv','w',encoding='utf-8') as f:
        csv_writer = csv.writer(f)
        csv_writer.writerow(['电影名称','评分','评价人数','导演','电影信息'])

        with ThreadPoolExecutor(max_workers=10) as executor:
            for i in range(0,226,25):
                url = f'https://movie.douban.com/top250?start={i}'
                executor.submit(main1, url)
                print(f'正在写入地址为{url}的电影相关信息')
                time.sleep(1.5)
    print('已完成全部工作')
