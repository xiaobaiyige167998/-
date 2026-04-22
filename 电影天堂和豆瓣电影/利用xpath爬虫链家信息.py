import requests
from lxml import etree
import re

# if '__name__' == '__main__':
url = 'https://weihai.lianjia.com/ershoufang/'
headers = {
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36",
    'Referer':'https://weihai.lianjia.com/'
}
# repn = requests.get(url,headers=headers,timeout=10)
# repn.raise_for_status() #检查状态码
# repn.encoding='utf-8'
# repns = repn.text
# obj = re.compile(r'<span class="">(?P<jg>.*?)</span>')
# repns = obj.finditer(repns)
# for i in repns:
#     print(i.group('jg'))

try:
    repn = requests.get(url,headers=headers,timeout=10)
    repn.raise_for_status() #检查状态码
    repn.encoding='utf-8'
    page_text = repn.text

except Exception as e:
    print(f'错误{e}')
    exit()

tree = etree.HTML(page_text)
li_list = tree.xpath('//li[contains(@class,"clear")]')

# if not li_list:
#     li_list = tree.xpath('//ul[@class="sellListContent"/li]')

with open('lianjia.txt','w',encoding='utf-8') as f:
    for li in li_list:
        title_elem = li.xpath('.//div[@class="title"]/a/text()')
        price_elem = li.xpath('.//div[@class="priceInfo"]/div[@class="totalPrice totalPrice2"]/span/text()')
        f.write(f'{title_elem} 总价格{price_elem}\n')
        print(f'{title_elem} 总价格{price_elem}')
print('写入完成')