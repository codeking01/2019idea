import random
import urllib.request

headers={
    # 'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    # Accept-Encoding: gzip, deflate
    # 'Accept-Language': 'zh-CN,zh;q=0.9',
    # 'Cache-Control': 'max-age=0',
    # 'Connection': 'keep-alive',
    'Cookie': 'JpriceID=3E15F5BBC52E1BBD7FBDD1B1A7A1CD24',
    # 'Host': '210.31.141.105:8084',
    # 'Upgrade-Insecure-Requests': 1,
    # 'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4595.0 Safari/537.36'
}
proxies_pool = [
    {'http': '112.195.241.83: 3256'},
    {'http': '117.94.222.222: 3256'},
    {'http': '117.94.222.28	: 3256'}
]
url='http://210.31.141.105:8084/sysaqjyks/'
request=urllib.request.Request(url=url,headers=headers)
proxies = random.choice(proxies_pool)
# 加代理
handler = urllib.request.ProxyHandler(proxies=proxies)
opener = urllib.request.build_opener(handler)
# 响应服务器数据
response = opener.open(request)
content=response.read().decode('utf-8')
print(content)