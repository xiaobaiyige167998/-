# 1. 提取到主页面中的每一个电影背后的url地址
    # 1.拿到'2023新片精品'那一块的html代码
    # 2.从刚才拿到的html代码中提取href值

# 2.访问子网页，提取电影名称和下载地址
#     1.通过href访问各电影网页
    # 2.提取各电影的名称和下载地址
import re
import requests

# 拿到'2023新片精品'那一块的html代码
url = 'http://dytt8.net/index.htm'

repo = requests.get(url)
repo.encoding='gbk'
repos = repo.text

obj = re.compile(r'2023新片精品.*?<table width="100%" border="0" cellspacing="0"'
                 r' cellpadding="0">(?P<lj>.*?)</table>',re.S)

repn = obj.finditer(repos)

for i in repn:
    repns = i.group('lj')

# 从刚才拿到的html代码中提取href值
list = []
obj1 = re.compile(r"最新电影下载</a>]<a href='(?P<href>.*?)'>",re.S)

href = obj1.finditer(repns)
for f in href:
    # print(f.group('href'))
    list.append(f.group('href'))



# 通过href访问各电影网页
for k in list:
    url2 = f'http://dytt8.net{k}'
    repo2 = requests.get(url2)
    repo2.encoding='gbk'
    repos2 = repo2.text

# 提取各电影的名称和下载地址
    obj2 =re.compile(r'◎片　　名　(?P<pm>.*?)<br />.*?<font color=red>磁力链下载器：<a href="(?P<dz>.*?)" '
                     r'target="_blank"  title="qBittorrent">点击下载</a>',re.S)
    repn2 = obj2.finditer(repos2)
    for m in repn2:
        print(m.group('pm'))
        print(m.group('dz'))

