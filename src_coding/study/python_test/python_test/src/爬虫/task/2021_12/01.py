'''
@author king_xiong
@date 2021-12-29 18:38
'''
import requests
from lxml import etree

# if(requests.get('https://www.chemicalbook.com/'+etree.HTML(requests.get('https://www.chemicalbook.com/Search.aspx?keyword='+str(537-29-1)).text).xpath("//tr/td[1]//div/a[1]/@href")[0])==200):
# print(type(requests.get('https://www.chemicalbook.com/'+etree.HTML(requests.get('https://www.chemicalbook.com/Search.aspx?keyword='+str(537-29-1)).text).xpath("//tr/td[1]//div/a[1]/@href")[0]).status_code))
url = 'https://www.chemicalbook.com/Search.aspx?keyword=55156-16-6'
content = requests.get(url).text
tree = etree.HTML(content)
a = tree.xpath("//tr/td[1]//div/a[1]/@href")
if (len(a) ==0):
    print('afdas')
