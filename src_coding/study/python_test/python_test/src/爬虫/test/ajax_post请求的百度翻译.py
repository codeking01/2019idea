# https://fanyi.baidu.com/sug
import urllib.request

# 这个是post请求
base_url = 'https://fanyi.baidu.com/sug'

header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4595.0 Safari/537.36'
}
data = {
    'kw': 'sub'
}
import urllib.parse
# post请求的 数据必须进行编码
data=urllib.parse.urlencode(data).encode('utf-8') #编码
# 请求定制对象
requset = urllib.request.Request(url=base_url, data=data,headers=header)
# print(requset)
# 模拟服务器发送请求
response = urllib.request.urlopen(requset)
# print(response)
# 响应数据 decode 解码 和 encode 编码不是一个
content = response.read().decode('utf-8') #解码
# print(content)
import json
# load 针对的是句柄，将json格式的字符转换为dict，从文件中读取 (将string转换为dict)
# 例如a_json = json.load(open('demo.json','r'))
# loads()针对的是内存对象，将string转换为dict (将string转换为dict)
# a_dict = {'a':'1111','b':'2222'}
# json.dump(a_dict, open('demo.json', 'w')
# obj=json.loads(content)
# print(obj)
with open('fnayi.json','w',encoding='utf-8') as fp :
    fp.write(content)