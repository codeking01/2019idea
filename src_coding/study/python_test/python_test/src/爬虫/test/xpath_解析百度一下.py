import urllib.request
url='https://www.baidu.com/'
headers={
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4595.0 Safari/537.36'
}
request=urllib.request.Request(url=url,headers=headers)
response=urllib.request.urlopen(request)
content=response.read().decode('utf-8')
# print(content)
from lxml import etree
tree=etree.HTML(content)
result=tree.xpath('//input[@id="su"]/@value')[0]
# xpath 的返回值是一个列表类型的返回值 可以通过修改下标获取内容
print(result)