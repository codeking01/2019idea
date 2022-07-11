import urllib.request

# 加入handler 来访问百度
url='https://wwww.baidu.com'
headers={
     'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4595.0 Safari/537.36'
}

request=urllib.request.Request(url=url,headers=headers)

# handler   build_opener    open
import faulthandler
# 获取handler对象
handler=urllib.request.HTTPHandler()
# 获取opener对象
opener=urllib.request.build_opener(handler)
# 调用open（）返回
response=opener.open(request)
content=response.read().decode('utf-8')
print(content)

