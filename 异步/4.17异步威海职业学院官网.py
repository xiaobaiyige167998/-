import requests
from lxml import etree
import asyncio
import aiohttp
import aiofiles

# 步骤：
#     1.对官网进行请求获取html
#     2.获取通知公告中每一个公告的href值
#     3.将https://www.whvc.edu.cn/与href值拼起来，形成新的url
#     4.获取每一个公告的浏览量




def get_url(url):
    resp = requests.get(url)
    resp.encoding='utf-8'
    resp = resp.text
    return resp




def get_href(html):
    href_list = []
    root = etree.HTML(html)
    ul = root.xpath('//ul[@class="news_list clearfix"]/li')
    for li in ul:
        href = li.xpath('.//a/@href')
        if href:
            url = href[0]
            if '/2026/0' in url:
                href_list.append(url)
    # print(href_list)
    return href_list

async def all_Download(find_url):
    async with aiohttp.ClientSession() as session:
        async with session.get(find_url) as resp:
            html = await resp.text()
            html = etree.HTML(html)
            lll = html.xpath('//span[@class="WP_VisitCount"]/text()')[0]
            print(f'浏览量为 {lll}')



async def Download(href_list):
    async with asyncio.TaskGroup() as tg:
        for find_href in href_list:
            href_url = 'https://www.whvc.edu.cn' + find_href
            tg.create_task(all_Download(href_url))



if __name__ == '__main__':
    url = 'https://www.whvc.edu.cn/'
    a = get_href(get_url(url))
    asyncio.run(Download(a))


