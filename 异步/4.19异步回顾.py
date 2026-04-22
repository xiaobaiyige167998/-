import asyncio
import aiohttp
import aiofiles
import requests
from lxml import etree

url = 'https://www.baidu.com/'
async def get_url(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            content = await resp.text()
            print(content)



if __name__ == '__main__':
    async with asyncio.TaskGroup() as tg:
        tg.create_task()

