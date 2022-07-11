import urllib.request
import urllib.parse

headers={
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4595.0 Safari/537.36'
    #防止 UA反爬
}
data={
    'wd':'周杰伦'
}
base_url='https://www.baidu.com/s?'
new_data =urllib.parse.urlencode(data)
url=base_url+new_data
print(url)
request=urllib.request.Request(url =url,headers=headers)
response=urllib.request.urlopen(request)
content=response.read().decode('utf-8')
print(content)