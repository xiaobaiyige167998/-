import requests
from pyquery import PyQuery

def requests_get_url(url):
    resp = requests.get(url)
    resp.encoding='utf-8'
    return resp.text

def pyquery_get(html):
    doc = PyQuery(html)
    co_li = doc('.col-xs-6.col-sm-4.col-md-3.col-lg-3').items()
    for co in co_li:
        name = co('article > h3 > a').text()
        href = co('article > div:nth-child(1) > a').attr('href')
        pirc = co('article > div[class="product_price"] > p').text()
        print(pirc)
def main():
    # 1.获取网页源代码
    url = 'https://books.toscrape.com/'
    html = requests_get_url(url)
    # 2.解析网页源代码，提取数据
    pyquery_get(html)

if __name__ ==  "__main__":
    main()