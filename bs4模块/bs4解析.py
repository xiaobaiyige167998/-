from bs4 import BeautifulSoup


html = """
    <ul>
    <li><a href="zhangwuji.com">张无忌</a></li>
    <li id="abc"><a href="zhouxingchi.com">周星驰</a></li>
    <li><a href="zhubajie.com">猪八戒</a></li>
    <li><a href="wuzetian.com">武则天</a></li>
</ul>
"""

# 初始化BeautifulSoup对象
page = BeautifulSoup(html,'html.parser')     # html.parser是用来解释传入的是html代码，进行解析
li = page.find('li',attrs={'id':'abc'})
a = li.find('a')
print(a.text)
print(a.get('href'))
