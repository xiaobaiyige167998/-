import asyncio
import aiohttp

urls = [
    'https://file1.qxapi.asia/view.php/7ef6d291a999978441d0802c1dd38376.png',
    'https://file1.qxapi.asia/view.php/2cd700a75ba3023e7ebda9c73da0dfea.png&rkey=CAMSMDX6qCSWNlaXuOaGa_pTF4Q2FtlI-OJ5m3Gxre_VikyJg',
]

async def aiodownload(url):
    # 步骤：
    #     1.发送请求
    #     2.获取请求的内容
    #     3.下载图片
    name = url.split('/')[-1]
    async with aiohttp.ClientSession() as session:   #相当于request
        async with session.get(url) as resp:   #发送并获取请求的内容
            with open(name,'wb') as l:     #下载图片
                l.write(await resp.content.read())   #因为下载时不占用cpu，所以可以加上await
    print(name,'成功')



async def main():
    async with asyncio.TaskGroup() as f:
        for url in urls:      #调用各链接并生成协程对象
            f.create_task(aiodownload(url))


if __name__ == '__main__':
    asyncio.run(main())