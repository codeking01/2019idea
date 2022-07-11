import requests

url='https://www.baidu.com/'
headers={
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.54 Safari/537.36'
}

# get 请求的是params
response=requests.get(url=url,headers=headers)
# 这个是获取网页的源码
response.encoding='utf-8'
content=response.text
print(content)


