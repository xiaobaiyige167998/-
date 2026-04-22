import requests
from concurrent.futures import ThreadPoolExecutor
from pyquery import PyQuery

# 基本步骤：
#     1.获取单页的url
#     2.获取单页url里面的第一个电影的href
#     3.将https://ssr1.scrape.center与获取的电影href值拼接成新的url
#     4.获取电影信息
#
#
# 进阶步骤:
#     1.获取每一页的url
#     2.获取每一页url里面每一个电影的href
#     3.将https://ssr1.scrape.center/与获取的每一个电影的href值拼接成新的url
#     4.获取电影信息





# 获取单页url里面的第一个电影的href
def href(html):
    href_list = []
    p = PyQuery(html)
    div_list = p('.el-card.item.m-t.is-hover-shadow')
    for a in div_list.items():
        href_list.append(a('a').attr('href'))
    return href_list


# 将https://ssr1.scrape.center与获取的电影href值拼接成新的url
def splicing_url(href_list):
    Movie_url_list = []
    for href in href_list:
        Movie_url = 'https://ssr1.scrape.center' + href
        Movie_url_list.append(Movie_url)
    return Movie_url_list

# 中间商
def zjs(Movie_url_list):
    with ThreadPoolExecutor(10) as t:
        for Information in Movie_url_list:
            t.submit(Movie_Information,Information)



# 获取电影信息
def Movie_Information(Information):
    resp = requests.get(Information)
    resp.encoding='utf-8'
    resp = resp.text
    p1 = PyQuery(resp)
    text = p1('.drama')('p').text()
    print(text)




if __name__ == '__main__':
    # 获取每一页的url
    with ThreadPoolExecutor(5) as tp:
        for i in range(1,10):
            url = f'https://ssr1.scrape.center/page/{i}'
            resp = requests.get(url)
            resp.encoding='utf-8'
            resp = resp.text
            a= href(resp)
            b= splicing_url(a)
            tp.submit(zjs,b)