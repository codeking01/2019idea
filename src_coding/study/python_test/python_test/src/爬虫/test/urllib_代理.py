import urllib.request

url = 'https://www.baidu.com/s?wd=ip'
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4595.0 Safari/537.36',
}
request=urllib.request.Request(url=url,headers=headers)
proxies={
    # 'key' : 'value'
    'http':'114.230.107.75:3256'
}
handler=urllib.request.ProxyHandler(proxies=proxies)
opener=urllib.request.build_opener(handler)
response=opener.open(request)


#  模拟浏览器访问服务器
# response=urllib.request.urlopen(request)
# 相应数据
content=response.read().decode('utf-8')
# print(content)
with open('ip.html','w',encoding='utf-8') as fp:
    fp.write(content)