from bs4 import BeautifulSoup
import requests

f = open('bs4实战.data','w',encoding='utf-8')

headers = {
"user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/146.0.0.0 Safari/537.36 Edg/146.0.0.0"
}
url = 'https://movie.douban.com/chart'
repo = requests.get(url,headers=headers)

hl = BeautifulSoup(repo.text,'html.parser')
dy = hl.find_all('a',attrs={'class':'nbg'})
for i in dy:
    href = i.get('href')
    # print(href)
    f.write(f'{href}\n')

f.close()