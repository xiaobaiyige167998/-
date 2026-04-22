import requests
# 1.获取conId
# 2.拿到VideosStatus返回的json --> srcUrl
# 3.修正srcUrl
# 4.下载视频

# 1.
url = 'https://www.pearvideo.com/video_1805569'
conId = url.split('_')[1]
# 2.
VideosStatus_url =  f"https://www.pearvideo.com/videoStatus.jsp?contId={conId}&mrd=0.4916747589942402"
headers = {
    "referer":"https://www.pearvideo.com/video_1805569"
}
resp = requests.get(VideosStatus_url,headers=headers).json()
systemTime = resp['systemTime']
srcUrl = resp['videoInfo']['videos']['srcUrl']
# 3.
srcUrl = srcUrl.replace(systemTime,f'cont-{conId}')
# 4.下载视频     注意：下载图片或者视频都必须进行异常请求获取响应体，content为响应
zz_Url = requests.get(srcUrl)
with open('视频.mp4','wb') as f:
    f.write(zz_Url.content)



# 防盗链即referer，必须从我的地址进入网站才可以获取，如果直接进入网站则不行