import urllib.request
import json
import jsonpath
# https://dianying.taobao.com/cityAction.json?activityId&_ksTS=1632214089734_143&jsoncallback=jsonp144&action=cityAction&n_s=new&event_submit_doGetAllRegion=true
# Request Method: GET
# user-agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4595.0 Safari/537.36
headers={
    # 带 ： 的请求头一般不好使
    # ':method: GET': '',
    # ':path: /cityAction.json?activityId&_ksTS=1632214089734_143&jsoncallback=jsonp144&action=cityAction&n_s=new&event_submit_doGetAllRegion=true': '',
    # ':scheme: https': '1',
    'accept': 'text/javascript, application/javascript, application/ecmascript, application/x-ecmascript, */*; q=0.01',
    'accept-language': 'zh-CN,zh;q=0.9',
    'cookie': 'tg=0; miid=1540501606590726636; cna=KxH+FgubmHcCAXzkuXP0V7Qi; thw=cn; hng=CN%7Czh-CN%7CCNY%7C156; tracknick=%5Cu56DE%5Cu5FC6%5Cu80DC%5Cu4F3C%5Cu5FC6; enc=s%2FXjyWs2xlMhI8DspJAgTNoDrAk3ZskiQU6s2P9Vp048xB3acCTHLgFofQwznyV2nPEh0Ov7vLz7lZX52SzrZg%3D%3D; UM_distinctid=17a13dd505c2ad-099370fbd93a73-68517129-144000-17a13dd505d393; t=8f50176630a895065afa68b22ec5df94; sgcookie=E1009OKDMzc3NF92l5e2yUvVQSYOz%2F%2Fwk52WFlfGY5cIx4ic9HfPjQbQW%2F57tYWiheHqKhNnwFqQSBMHDZXWiKNHKi%2BkZhlR4FRQ6DFFg2UZIdM%3D; uc3=nk2=2ABpe80Ezpm%2FWg%3D%3D&id2=UUwTqQvO7y%2BPBA%3D%3D&lg2=U%2BGCWk%2F75gdr5Q%3D%3D&vt3=F8dCujC9AvYTAEyxt1k%3D; lgc=%5Cu56DE%5Cu5FC6%5Cu80DC%5Cu4F3C%5Cu5FC6; uc4=nk4=0%402jVKTPzn90RkG%2FKNBhBsO%2FWkShgK&id4=0%40U27M2zu8IgG5c463YU0fFSS5wh41; _cc_=U%2BGCWk%2F7og%3D%3D; mt=ci=-1_0; _m_h5_tk=ee218d831faa59b5a6de3b898a33d97c_1632155082706; _m_h5_tk_enc=efdf54d2619323116ffcdcf1cdf048a5; xlly_s=1; CNZZDATA1256793290=1675484192-1632204334-https%253A%252F%252Fwww.baidu.com%252F%7C1632204334; cookie2=257b41fb68c12ab13dd966ef7a37bff5; v=0; _tb_token_=35e6133f0baed; uc1=cookie14=Uoe3dYNYl2pRLg%3D%3D; tfstk=cCfFBF124WFeEpR7HBOzNMWa1q9daCtkcf82K9bTmFnxVyJp0s0Z2FXrsF8yD5vh.; l=eBOtuwhrjNyjY3CMBO5alurza77tWQRb4VFzaNbMiInca6ThteI0DNCL1LOJSdtjgtCYAetrOcbqkRLHR3xg5c0c07kqm0JjUxvO.; isg=BNTUgQtNSc52CNzSWIwQBZN-pRJGLfgXSnctRG63l9_QWXSjljx6p5nXWVFB_DBv',
    'referer': 'https://dianying.taobao.com/',
    'sec-ch-ua': '"Chromium";v="94", "Google Chrome";v="94", ";Not A Brand";v="99"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': "Windows",
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4595.0 Safari/537.36',
    'x-requested-with': 'XMLHttpRequest'
}
url='https://dianying.taobao.com/cityAction.json?activityId&_ksTS=1632214089734_143&jsoncallback=jsonp144&action=cityAction&n_s=new&event_submit_doGetAllRegion=true'

request=urllib.request.Request(url=url,headers=headers)
response=urllib.request.urlopen(request)
content=response.read().decode('utf-8')
content=content.split("(")[1].split(")")[0]
# print(content)
with open('淘票票.json','w',encoding='utf-8') as fp:
    fp.write(content)
obj=json.load(open('淘票票.json','r',encoding='utf-8'))
ret=jsonpath.jsonpath(obj,'$.returnValue..regionName')
print(ret)

