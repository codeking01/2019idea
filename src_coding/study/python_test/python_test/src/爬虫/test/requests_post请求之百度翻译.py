import requests
import random
import json

# 百度翻译 是 post请求
url = 'https://fanyi.baidu.com/sug'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.54 Safari/537.36'
}
data = {
    'kw': 'eye'
}
proxies_pool = [
    {'http': '112.195.241.83: 3256'},
    {'http': '117.94.222.222: 3256'},
    {'http': '117.94.222.28	: 3256'}
]
# 这个下面的choice后面的东西是一个参数，不要用字符串（比如加引号）
proxies = random.choice(proxies_pool)
# post 请求 要用post发
response = requests.post(url=url, data=data, headers=headers)
# 响应服务器数据
content = response.text
print(content)

# obj=json.loads(content,encoding='utf-8')
# print(obj)

obj =str(json.loads(content))
print(obj)
with  open('./text/baidufanyi.json', 'w', encoding='utf-8') as fp:
    fp.write(obj)
