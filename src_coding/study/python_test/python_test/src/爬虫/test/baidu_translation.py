import urllib.request
import urllib.parse
import json

# 注意写的Url是自己 post请求需要的url；否则会报错： urllib.error.HTTPError: HTTP Error 404: Not Found
url = 'https://fanyi.baidu.com/v2transapi?from=en&to=zh'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4595.0 Safari/537.36',
    'Accept': '*/*',
    # 'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Connection': 'keep-alive',
    'Content-Length': '134',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    # cookie是最重要的
    'Cookie': 'BIDUPSID=EA2A87B13B3C4B243BAC784520C77701; PSTM=1553512033; REALTIME_TRANS_SWITCH=1; FANYI_WORD_SWITCH=1; SOUND_SPD_SWITCH=1; HISTORY_SWITCH=1; SOUND_PREFER_SWITCH=1; BDUSS=VFwRkY1U3Z2d1VXfjk2VkZBQU9Qdml6STJoMm05eW5-eEg4VkxPNn5GM1llcUZmRVFBQUFBJCQAAAAAAAAAAAEAAACW-QFMYWd1Z2FnAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAANjteV~Y7Xlfc; BDUSS_BFESS=VFwRkY1U3Z2d1VXfjk2VkZBQU9Qdml6STJoMm05eW5-eEg4VkxPNn5GM1llcUZmRVFBQUFBJCQAAAAAAAAAAAEAAACW-QFMYWd1Z2FnAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAANjteV~Y7Xlfc; BAIDUID=D46BFF2E80FB7AA69747216AFEAD2F7E:FG=1; __yjs_duid=1_a959f8185db879fc55a51e530ba314e01619354273237; BAIDUID_BFESS=D46BFF2E80FB7AA69747216AFEAD2F7E:FG=1; BDRCVFR[w-kNo__JL0t]=1jmUUpB1KcCmh7GmLNEmi4WUvY; BDRCVFR[xoix5KwSHTc]=9xWipS8B-FspA7EnHc1QhPEUf; delPer=0; PSINO=2; Hm_lvt_64ecd82404c51e03dc91cb9e8c025574=1631267016,1631715283,1631750193,1631768426; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; BA_HECTOR=8ga101210hah8h016b1gk6fb00r; BDRCVFR[feWj1Vr5u3D]=I67x6TjHwwYf0; H_PS_PSSID=34650_34445_31254_34552_33848_34584_34092_34106_26350_34421_34691; Hm_lpvt_64ecd82404c51e03dc91cb9e8c025574=1631796919; __yjs_st=2_MzBjOTYxYjAwMjAxOTgxOTIyMTBiN2ZmOTA4Y2U1ZjM1ZDIyMmJkYjE3ODIyZDE3ZTI2YWU0ZDM5MmM0M2FmZTZjNjU5NTc0ZDhlZjVjYTg2NTgyODhmZTZhM2RiYWZkYWZlMzcxNmM5YWE3YzFjNzY2MzNjNDI0MzdiNjk2ZDgwMzRhYTY3ODZjNDgyY2I5ZDJiNjBkZDkzMTYyZjA1YTIzZjg0NjU4ZTBiMjVhOTQxOWUyOTYwZmRjYmIzOTgyNTI0MmY1MTBiOTQ0YjJjZWQzM2ZjN2RiNmVmYThkZmNkNGRjYWY1YzBhMWRiNGE5ODVkNTE4M2NkZjk5MTUyZF83Xzg5OTZjMWJi; ab_sr=1.0.1_ZTNjMzA5OTI0NDFjOGE4MGFhMjg2MjMwNWM4NjcxMGZkM2JjMDZlYzIzNDcyZDU0ODU2YTBhYTBiY2FiMzYzZTU0MDFlYTdiMjExMjY3YzMxZTQ5YWEyOTFjMDJiOGU2OGFjZmRjYWE1NWZiMTFkOTRhNzZmNDEzZWVmNzgzZTA0N2RmYTIyNjdhZDBjMmMyZjVmZWY1NTBlNjU0MTAwYzY2NjBkYTExNGY0ODRkZjhiNmMzNzdiMWFjOTJlOWMz',

    'Host': 'fanyi.baidu.com',
    'Origin': 'https://fanyi.baidu.com',
    'Referer': 'https://fanyi.baidu.com/translate?aldtype=16047&query=&keyfrom=baidu&smartresult=dict&lang=auto2zh',
    'sec-ch-ua': '"Chromium";v="94", "Google Chrome";v="94", ";Not A Brand";v="99"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': "Windows"'',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4595.0 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest'
}
data = {
    'from': 'en',
    'to': 'zh',
    'query': 'sub',
    'transtype': 'realtime',
    'simple_means_flag': '3',
    'sign': '658484.978693',
    'token': '883d6548e6b0906375d955131c6212ae',
    'domain': 'common'
}
# urlencode 是在urllib.parse里面的方法
data = urllib.parse.urlencode(data).encode('utf-8')

# 请求对象定制
request = urllib.request.Request(url=url, data=data, headers=headers)

# 模拟向服务器发送请求
response = urllib.request.urlopen(request)

# 获取响应
content = response.read().decode('utf-8')

# print(contend)

obj = json.loads(content)
print(obj)
