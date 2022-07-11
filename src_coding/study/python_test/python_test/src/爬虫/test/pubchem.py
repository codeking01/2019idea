import urllib.request
from lxml import etree

url='pubchem.html'
headers={
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.54 Safari/537.36'
}
# get 请求的是params
# request=urllib.request.Request(url=url,headers=headers)
# # 这个是获取网页的源码
# response=urllib.request.urlopen(request)
# content=response.read().decode('utf-8')
# print(content)
html_tree=etree.parse('pubchem.html')
print(html_tree)
# name_list=tree.xpath('//div//a[@class=" capitalized"]/@href')
# print(name_list)
