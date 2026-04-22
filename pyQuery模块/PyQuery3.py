import requests
from pyquery import PyQuery


def requests_get_url(url):
    resp = requests.get(url)
    resp.encoding='utf-8'

    return resp.text


def pyquery_get_html(html,f):
    doc = PyQuery(html)
    for i in range(1,12):
        div_list = doc(f'.codelist.codelist-desktop.cate{i} a.item-top')
        for div in div_list.items():
            name = div('h4').text().strip()
            xx_text = div('strong').text().strip()
            href = div('a').attr('href').strip()
            href = href.strip('//')
            # print(f'{name},{xx_text}\n')
            f.write(f'{name},{xx_text},{href}\n')



def main():
    # 1.获取网页源代码
    url = 'https://www.runoob.com/'
    html = requests_get_url(url)
    # 2.解析网页源代码，获取数据
    with open('PyQuery3.csv', 'w', encoding='utf-8-sig') as f:
        f.write('课程名字，课程描述，课程链接\n')
        pyquery_get_html(html, f)

if __name__ == '__main__':
    main()