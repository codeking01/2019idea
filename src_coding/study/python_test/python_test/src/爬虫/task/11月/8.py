import requests
import requests as requests

from lxml import etree

# url='http://www.dianping.com/shop/H5cGIBA4YVFFBuKk'
url='http://www.dianping.com/shop/l6y9rHNsA0KdKUMi'
headers={
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36',
    'Cookie':'_lxsdk_cuid=17c7f907122c8-005a3d1714b78c-b7a1438-144000-17c7f907122c8; _lxsdk=17c7f907122c8-005a3d1714b78c-b7a1438-144000-17c7f907122c8; _hc.v=751dd7ad-f61c-e41b-0401-95d1866ae493.1634227745; s_ViewType=10; ctu=1dc952f673738fa47d20413160405840235920484dc849760c4a66b318dd0f6b; fspop=test; cy=344; cye=changsha; aburl=1; Hm_lvt_dbeeb675516927da776beeb1d9802bd4=1635694823; Hm_lvt_4c4fc10949f0d691f3a2cc4ca5065397=1635694848; dplet=8cd55c58151c3c226f08a7e0412fb5bc; dper=7d41a91163639f439fad4499101f178c94c42a6965f2cff10a510d206137bd96cceb4d34a256342ec736bdddbb7e80c8752983ed7cdda14afec03f9ef8767274d3fcfe72e562dec27f828bb66a5a6690fa47fc2193f8d56ddcd930671457c911; ua=dpuser_4260155846; ll=7fd06e815b796be3df069dec7836c3df; _lx_utm=utm_source%3DBaidu%26utm_medium%3Dorganic; Hm_lvt_602b80cf8079ae6591966cc70a3940e7=1635742062,1635761268,1635763416,1635950312; Hm_lpvt_602b80cf8079ae6591966cc70a3940e7=1635950352; _lxsdk_s=17ce63cb8d8-15e-e0a-397%7C%7C101',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Content-Type': 'text/html;charset=UTF-8',
    'Referer': 'http://www.dianping.com/changsha/ch10/g117r7964',
}
# 字体加密的处理
dic = {'uefb0': '0', 'ue9e5': '2', 'ue838': '3', 'ue364': '4', 'uf128': '5',
       'uf639': '6', 'uf440': '7', 'ue174': '8', 'ue7c3': '9', }



# request=urllib.request.Request(url=url,headers=headers)
response = requests.get(url,headers=headers)
tree=etree.HTML(response.text)
# content=tree.xpath('//div[@class="brief-info"]//d//text()')
# 人均
price_content=tree.xpath('//span[@id="avgPriceTitle"]/d/text()')
# 如果没有人均信息 返回--，处理111
if len(price_content)==0:
    price=tree.xpath('//span[@id="avgPriceTitle"]/text()')[0].split(':')[1]
# 处理1开头的
elif(len(tree.xpath('//span[@id="avgPriceTitle"]/text()')[0])>4):
    price_top=tree.xpath('//span[@id="avgPriceTitle"]/text()')[0].split(':')[1]
    price_mid=tree.xpath('//span[@id="avgPriceTitle"]/d/text()')
    # 先获取中间元素的长度
    lenth=len(price_mid)
    # 101和110
    if(lenth==1):
        price_mid=price_mid[0].encode('raw_unicode_escape').decode('utf8').replace('\\','')
        price_mid=dic[price_mid]
    # 100
    else:
        price_mid_1=price_mid[0].encode('raw_unicode_escape').decode('utf8').replace('\\','')
        price_mid_1=dic[price_mid_1]
        price_mid_2=price_mid[1].encode('raw_unicode_escape').decode('utf8').replace('\\','')
        price_mid_2=dic[price_mid_2]
        price_mid=price_mid_1+price_mid_2

    price_base=tree.xpath('//span[@id="avgPriceTitle"]/text()')[1]
    print('**')
    print(price_base)
    price=price_top+price_mid+price_base
# 处理1结尾的
elif(tree.xpath('//span[@id="avgPriceTitle"]/text()')[1][0]=='1'):
    price_mid=tree.xpath('//span[@id="avgPriceTitle"]/d/text()')
    # 先获取中间元素的长度
    lenth=len(price_mid)
    # 101和110
    if(lenth==1):
        price_mid=price_mid[0].encode('raw_unicode_escape').decode('utf8').replace('\\','')
        price_mid=dic[price_mid]
    # 100
    else:
        price_mid_1=price_mid[0].encode('raw_unicode_escape').decode('utf8').replace('\\','')
        price_mid_1=dic[price_mid_1]
        price_mid_2=price_mid[1].encode('raw_unicode_escape').decode('utf8').replace('\\','')
        price_mid_2=dic[price_mid_2]
        price_mid=price_mid_1+price_mid_2
    price_base=tree.xpath('//span[@id="avgPriceTitle"]/text()')[1]
    price=price_mid+price_base
# 处理010
elif(tree.xpath('//span[@id="avgPriceTitle"]/text()')[1]=='1'):
    price_top=tree.xpath('//span[@id="avgPriceTitle"]/d/text()')
    price_top=price_top[0].encode('raw_unicode_escape').decode('utf8').replace('\\','')
    price_top=dic[price_top]
    price_base=tree.xpath('//span[@id="avgPriceTitle"]/d/text()')[1]
    price_base=price_base.encode('raw_unicode_escape').decode('utf8').replace('\\','')
    price_base=dic[price_base]
    price=price_top+'1'+price_base+'元'
# 处理
else:
    price=tree.xpath('//span[@id="avgPriceTitle"]/d/text()')
    # 先获取中间元素的长度
    lenth=len(price)
    # 101和110
    if(lenth==1):
        price=price[0].encode('raw_unicode_escape').decode('utf8').replace('\\','')
        price=dic[price]+'元'
    # 00 和000
    elif(lenth==2):
        price_1=price[0].encode('raw_unicode_escape').decode('utf8').replace('\\','')
        price_1=dic[price_1]
        price_2=price[1].encode('raw_unicode_escape').decode('utf8').replace('\\','')
        price_2=dic[price_2]
        price=price_1+price_2+'元'
    else:
        price_1=price[0].encode('raw_unicode_escape').decode('utf8').replace('\\','')
        price_1=dic[price_1]
        price_2=price[1].encode('raw_unicode_escape').decode('utf8').replace('\\','')
        price_2=dic[price_2]
        price_3=price[2].encode('raw_unicode_escape').decode('utf8').replace('\\','')
        price_3=dic[price_3]
        price=price_1+price_2+price_3+'元'
print(price)

# price=price_top+'1'+price_bottom+'元'
# list1=['\ue174', '\uf128', '\ue174', '\uf440', '\ue174', '\uf440']
# a=list1[0]
# b=a.encode('raw_unicode_escape').decode('utf8').replace('\\','')
# print(b)
# 分别取  分别找就行了

dic_con = {'*': '0','ue7c3':'1', '*': '2', '*': '3', 'uf440': '4', '*': '5',
       '*': '6', '*': '7', '*': '8', '*': '9', }
# 口味 环境 服务 的汇总
content=tree.xpath('//span[@id="comment_score"]')
# print(content)
taste_1=content[0].xpath('./span[3]//text()')[1].encode('raw_unicode_escape').decode('utf8').replace('\\','')
taste_2=content[0].xpath('./span[1]//text()')[3].encode('raw_unicode_escape').decode('utf8').replace('\\','')

print(taste_1)
print(content[0].xpath('./span[2]//text()'))
