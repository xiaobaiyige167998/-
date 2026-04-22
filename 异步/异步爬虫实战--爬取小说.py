# 'https://apibi.cc/api/booklist?id=135539'  获取小说章节的名字
# 'https://apibi.cc/api/chapter?id=135539&chapterid=1'  获取小说章节的内容


# 步骤：
#     1.获取小说章节的名字
#     2.获取小说章节的内容
#     3.下载内容


import requests
import json
import aiohttp
import asyncio
import aiofiles


folder = "小说"
def get_url(url):
    resp = requests.get(url).json()
    return resp['list']


async def all_Download(all_name):
    async with aiohttp.ClientSession() as session:
        async with asyncio.TaskGroup() as tg:
            n = 1
            for name in all_name:
                url1 = f'https://apibi.cc/api/chapter?id=135539&chapterid={n}'
                tg.create_task(Download(url1,name,session))
                n+=1

async def Download(url,name,session):
        file_path = f"{folder}/{name}.txt"
        async with session.get(url) as resp:
            data =await resp.text()
            data = json.loads(data)['txt']
            async with aiofiles.open(file_path,'w',encoding='utf-8') as g:
                await g.write(data)



if __name__ == '__main__':
    url = 'https://apibi.cc/api/booklist?id=135539'
    asyncio.run(all_Download(get_url(url)))



