import requests
import re

url = 'https://www.0-c.cc/download3.html'

repo = requests.get(url)

repos = repo.text

obj = re.compile(r'<a href="(?P<lj1>.*?) target="_blank"',re.S)

result = obj.finditer(repos)

list = []

for i in result:
    list.append(i.group('lj1'))

print(list)