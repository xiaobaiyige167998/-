import requests
from pyquery import PyQuery

def requests_get_url(url):
    resp = requests.get(url)
    # resp.encoding='utf-8'

    return resp.text

def html_pyquery(html):
    doc = PyQuery(html)
    co_list = doc('div.col-12.col-md-6').items()
    for co in co_list:
        name = co('a').text()
        href = co('a').attr('href')
        print(name)
        print(href)
    return



def main():
    # 1.获取网页源代码
    url = 'https://www.xbiquge.com.cn/'
    html = requests_get_url(url)
    # 2.解析网页源代码，获取数据
    html_pyquery(html)
if __name__ == '__main__':
    main()