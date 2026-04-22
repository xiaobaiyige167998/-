import asyncio
import time
import aiohttp
import aiofiles
import json
import requests


# 步骤：
#     1.获取小说所有章节名字
#     2.获取小说章节内容
#     3.保存小说内容

folder = "小说"


def get_url(url):
    resp = requests.get(url).json()
    return resp['list']               #返回name的全部列表


# 把所有章节的请求进行异步
async def all_Download(all_name):
    async with aiohttp.ClientSession() as session:
        async with asyncio.TaskGroup() as tg:
            n=1
            for name in all_name:
                url = f'https://apibi.cc/api/chapter?id=135539&chapterid={n}'
                tg.create_task(Download(url,name,session))
                n+=1


# 最后所有异步操作进行下载
async def Download(url,name,session):
    file_path = f"{folder}/{name}.txt"
    try:
        async with session.get(url) as resp:
            data = await resp.text()
            data = json.loads(data)['txt']
            async with aiofiles.open(file_path,'w',encoding='utf-8') as g:
                await g.write(data)
        print(f"已下载：{name}")
    except Exception as e:
        print(e)

if __name__ == '__main__':
    url = 'https://apibi.cc/api/booklist?id=135539'
    t1 = time.time()
    asyncio.run(all_Download(get_url(url)))
    t2 = time.time()
    print(t2-t1)


# # 总结： 1.首先对网站章节进行请求获取所有章节的name列表    （次要!!!!）
# #       2.把所有章节的请求全部进行异步操作 （主要！！！！）   通过一个单独的函数只进行异步操作！！！！
# #       3.最后通过一个总下载函数，只进行下载与保存  (第二主要！！！)
#         4.其实就all_Download()和Download()函数重要，get_url()函数在这里只光获取章节名称，用于区分后续小说写入的名字