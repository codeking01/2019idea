import urllib.request
# from lxml import etree
from bs4 import BeautifulSoup

url = 'https://www.starbucks.com.cn/menu/'
request = urllib.request.Request(url=url)
response = urllib.request.urlopen(request)
content = response.read().decode('utf-8')
soup=BeautifulSoup(content,'lxml')
# //ul[@class="grid padded-3 product"]//strong
# print(soup.find_all('strong'))
# grid padded-3 product strong -->可以直接改成strong
name_list=soup.select('strong')
# print(name_list)
for i in name_list:
    # print(i)
    # get_text() 获取文本信息
    name=i.get_text()
    print(name)

# print(content)
