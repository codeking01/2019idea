import random
import urllib.request

# https://www.baidu.com/s?ie=UTF-8&wd=ip
# get
url='https://www.baidu.com/s?ie=UTF-8&wd=ip'
header={
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4595.0 Safari/537.36, ',
    'Cookie':'BIDUPSID=EA2A87B13B3C4B243BAC784520C77701; PSTM=1553512033; sug=3; sugstore=1; ORIGIN=2; bdime=0; BDUSS=VFwRkY1U3Z2d1VXfjk2VkZBQU9Qdml6STJoMm05eW5-eEg4VkxPNn5GM1llcUZmRVFBQUFBJCQAAAAAAAAAAAEAAACW-QFMYWd1Z2FnAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAANjteV~Y7Xlfc; BDUSS_BFESS=VFwRkY1U3Z2d1VXfjk2VkZBQU9Qdml6STJoMm05eW5-eEg4VkxPNn5GM1llcUZmRVFBQUFBJCQAAAAAAAAAAAEAAACW-QFMYWd1Z2FnAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAANjteV~Y7Xlfc; BAIDUID=D46BFF2E80FB7AA69747216AFEAD2F7E:FG=1; __yjs_duid=1_a959f8185db879fc55a51e530ba314e01619354273237; BD_UPN=12314753; __sec_t_key=ee2cc316-5fe2-411b-97d1-2c5507e21e4a; BAIDUID_BFESS=D46BFF2E80FB7AA69747216AFEAD2F7E:FG=1; BD_HOME=1; H_PS_PSSID=34650_34445_34067_31254_34552_33848_34584_34106_26350_34421_34692; delPer=0; BD_CK_SAM=1; PSINO=2; H_PS_645EC=f8a5uTndEfpBUZ%2BfXvYvEDduhOnhFza9DwvvNJXc1rV7kqwwoy%2FTgdbX0CM; BA_HECTOR=20ahah0h2l2h2h0ldu1gkfsrf0r; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; COOKIE_SESSION=168890_1_8_8_1_11_1_0_7_9_12_1_0_0_0_0_1631716632_1631936294_1632105326%7C9%23835025_18_1631936293%7C9Host: www.baidu.com'
}
# 定制对象
request=urllib.request.Request(url=url,headers=header)
proxies_pool=[
    {'http':'112.195.241.83: 3256'},
    {'http':'117.94.222.222: 3256'}
]
proxies=random.choice(proxies_pool)
# 要用代理打开，所以引入了handler
handler=urllib.request.ProxyHandler(proxies=proxies)
# 把handler对象传给opener
opener=urllib.request.build_opener(handler)

def download(content) :
    with open('ip_new.html','w',encoding='utf-8') as fp:
        fp.write(content)

# 响应服务器请求
response=opener.open(request) #用的opener对象打开的
content=response.read().decode('utf-8')
# print(content)
download(content)





