import aiohttp
import asyncio


# 步骤：
#     1.发送请求
#     2.获取请求内容
#     3.下载图片
urls = [
    'https://images.pexels.com/photos/34577784/pexels-photo-34577784.jpeg',
    'https://images.pexels.com/photos/36671775/pexels-photo-36671775.jpeg',
    'https://images.pexels.com/photos/36408889/pexels-photo-36408889.jpeg'
]


async def aiodownload(url):
    name = url.split('/')[-1]
    async with aiohttp.ClientSession() as seesion:
        async with seesion.get(url) as resp:
            with open(name,'wb') as l:
                l.write(await resp.content.read())
    print(name,'成功')


async def main():
    for url in urls:
        async with asyncio.TaskGroup() as f:
            f.create_task(aiodownload(url))




if __name__ == '__main__':
    asyncio.run(main())