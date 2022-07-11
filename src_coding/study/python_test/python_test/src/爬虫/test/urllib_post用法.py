#post请求

import urllib.request
import urllib.parse
import json
#基本地址
url='https://fanyi.baidu.com/sug'
# 防止UA 反爬
headers= {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4595.0 Safari/537.36'
}
data= {
    'kw':'sub'
}
#post 请求的参数 必须进行编码，并且这个编码还得用decode（'utf-8'）
data=urllib.parse.urlencode(data).encode('utf-8')

request=urllib.request.Request(url=url,data=data,headers=headers)

#模拟服务器发请求
response=urllib.request.urlopen(request)
#响应服务器
content=response.read().decode('utf-8')
content=json.loads(content)
print(content)