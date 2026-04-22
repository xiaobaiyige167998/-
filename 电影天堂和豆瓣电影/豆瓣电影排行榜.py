import re
import requests

url = 'https://movie.douban.com/chart'

headers = {
"user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/146.0.0.0 Safari/537.36 Edg/146.0.0.0"
}

repo = requests.get(url,headers=headers)
repos = repo.text

obj = re.compile(r'<div class="pl2">.*?<span style="font-size:13px;">(?P<name>.*?)</span>.*?'
                 r'<span class="rating_nums">(?P<fs>.*?)</span>.*?'
                 r'<span class="pl">(?P<pj>.*?)</span>',re.S)

result = obj.finditer(repos)


with open('豆瓣电影排行榜.csv','w',encoding='utf-8') as f:
    f.write('电影名字,评分,多少人评价\n')

    for i in result:
        name = i.group("name")
        pg = i.group("pj")
        fs = i.group("fs")
        f.write(f'{name},{pg},{fs}\n')