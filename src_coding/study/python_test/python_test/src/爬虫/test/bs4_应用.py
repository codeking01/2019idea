from bs4 import BeautifulSoup
import urllib.request

# url = 'test_bs4.html'
# request = urllib.request.Request(url=url)
# response = urllib.request.urlopen(request)
# soup = BeautifulSoup(response.read().decode('utf-8'), 'lxml')
# soup.a 只会找第一个a标签
# soup.a.attrs -->  {'class': ['toindex'], 'href': '/'} 以一个字典类型返回
url = 'https://pubchem.ncbi.nlm.nih.gov/#query=57-27-2'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.54 Safari/537.36'
}

# soup=BeautifulSoup(open('pubchem.html',encoding='utf-8'),'lxml')
request=urllib.request.Request(url=url,headers=headers)
response=urllib.request.urlopen(request)
soup = BeautifulSoup(response.read().decode('utf-8'), 'lxml')

# print(soup.find('a',class_="a1")) #class_ 这个代表网页里面class（因为class是关键字）
# 找到所有的含有p的标签 soup.find_all('p')
# print(soup.find_all('p'))
# print(soup)
# print(find(a))
# print(soup)
# ########
# 属性选择器  [attribute=value]
# 层级选择器
# **
# div p 所有后代
# div>p 直接后代
# div,p 同级
# print(soup.select('li[id]'))
# print(soup.select('a,span'))
# print(soup.select('ul>li'))
# .select返回的是一个列表类型的
#   这个#后面加的是id的值
# obj.attrs.get('class') 获取这个属性中的class
# obj=soup.select('#p1')[0]
# print(obj.attrs.get('class'))

# ****************分割线
print(soup.find_all('a'))
# print(soup)