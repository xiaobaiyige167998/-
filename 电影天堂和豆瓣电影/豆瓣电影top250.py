import re
import requests

# 获取数据

nunms = range(0,250,25)

url = 'https://movie.douban.com/top250'
headers = {
    "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/146.0.0.0 Safari/537.36 Edg/146.0.0.0"
}

for p in range(0,250,25):

    repo = requests.get(url,headers=headers,params=f'?start={nunms}&filter=')

    pageSource = repo.text

    # 编写正则
    obj = re.compile(r'<div class="item">.*?<span class="title">(?P<name>.*?)</span>.*?<p>.*?导演: (?P<dao>.*?)&nbsp;.*?<br>(?P<year>.*?)&nbsp;.*?'
                     r'<span class="rating_num" property="v:average">(?P<score>.*?)</span>.*?<span>(?P<num>.*?)人评价</span>',re.S)
    result = obj.finditer(pageSource)

    for i in result:
        name = i.group("name")
        dao = i.group("dao")
        score = i.group("score")
        num = i.group("num")
        # 写入数据
        with open('豆瓣电影top250.csv', mode='a', encoding='utf-8') as f:
            f.write(f'{name},{dao},{score},{num}\n')
