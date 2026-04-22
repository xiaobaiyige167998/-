import requests
from concurrent.futures import ThreadPoolExecutor,ProcessPoolExecutor
from pyquery import PyQuery
import csv

f = open('线程池实战2.csv','w',encoding='utf-8')
csvwriter = csv.writer(f)


def get_url(url):
    resp = requests.get(url)
    resp.encoding='utf-8'
    html = PyQuery(resp.text)
    li = html('.col-xs-6.col-sm-4.col-md-3.col-lg-3 p:nth-child(1)').items()
    for i in li:
        price = i.text()
        csvwriter.writerow([price])
        print(f'{url}提取完成')







if __name__ == '__main__':
    with ThreadPoolExecutor(50) as l:
        for k in range(1,51):
            url = f'https://books.toscrape.com/catalogue/page-{k}.html'
            t = l.submit(get_url,url)
