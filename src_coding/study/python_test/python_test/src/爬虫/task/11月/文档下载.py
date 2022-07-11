import requests
from lxml import etree

url='http://www.doczj.com/doc/c462895ee55c3b3567ec102de2bd960590c6d970-6.html'
response=requests.get(url)
tree=etree.HTML(response.text)
a=tree.xpath('//p/text()')
print(a)