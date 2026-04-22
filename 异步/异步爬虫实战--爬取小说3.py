# 步骤：
#     1.获取小说章节
#     2.获取小说章节的id
#     3.通过小说章节的url和id进行拼接生成小说章节内容的url
#     4.下载小说内容


import requests
import asyncio
import aiohttp
import aiofiles
from pyquery import PyQuery


def name(url):
    name_list = []
    id_list = []
    resp = requests.get(url).json()
    resp = resp.get('data').get('chapters')
    for i in resp:
        name = i.get('title')
        id = i.get('id')
        name_list.append(name)
        id_list.append(id)
    return id_list

async def text(finally_url,n):
    async with aiohttp.ClientSession() as session:
        async with session.get(finally_url) as resp:
            html = await resp.text()
            doc = PyQuery(html)
            div = doc('div.article[data-v-2358fcd5] p')
            async with aiofiles.open(f'第{n}章','a',encoding='utf-8') as f:
                for nr in div.items():
                    await f.write(f'{nr.text()}\n')
            print('完成')



async def all_Download(id_list):
    n=1
    async with asyncio.TaskGroup() as tg:
        for id in id_list:
            finally_url = f'https://www.qimao.com/shuku/1879266-{id}'
            tg.create_task(text(finally_url,n))
            n+=1






if __name__ == '__main__':
    name_url = 'https://www.qimao.com/qimaoapi/api/book/chapter-list?book_id=1879266'
    asyncio.run(all_Download(name(name_url)))
