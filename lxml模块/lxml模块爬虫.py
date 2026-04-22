from lxml import etree
import requests

url = 'https://zb.lianjia.com/ershoufang/'
headers = {
"user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/146.0.0.0 Safari/537.36 Edg/146.0.0.0",
    "referer":"https://zb.lianjia.com/"
}

repn = requests.get(url,headers=headers)
repn.encoding='utf-8'
lj_txt = repn.text

# 解析html数据
root = etree.HTML(lj_txt)
# 获取html内容
houst_list = root.xpath('//li[contains(@class,"clear")]')
with open('链家信息.txt','w',encoding='utf-8') as f:
    for i in houst_list:
        nodes1 = i.xpath('./div[@class="info clear"]/div[@class="title"]/a/text()')
        nodes2 = i.xpath(
            './div[@class="info clear"]/div[@class="priceInfo"]/div[@class="totalPrice totalPrice2"]/span/text()')
        f.write(f"{nodes1},{nodes2}\n")