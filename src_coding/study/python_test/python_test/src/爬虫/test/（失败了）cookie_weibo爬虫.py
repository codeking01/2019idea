import urllib.request
# https://weibo.com/ajax/feed/unreadfriendstimeline?list_id=100013782693590&refresh=4&since_id=0&count=10
# https://weibo.com/u/3782693590/home
# GET请求 定制对象 可以拼接
# 'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4595.0 Safari/537.36'

url='https://weibo.com/'
header={
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4595.0 Safari/537.36',
    'cookie': 'SINAGLOBAL=7670206864374.667.1577076814719; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9W5Z520bFFmNICriv8w7D4-u5JpX5KMhUgL.FoeN1hzc1Kef1K52dJLoIEBLxK-L12eL1KMLxKqLBKzLBKqLxKqL1-eL1h.LxK.L1-zLB-2t; ALF=1663468454; SSOLoginState=1631932455; SCF=AiCajMTWJr9IyLKLtyGejQ4KG-UoHWDBJmOAS9QAZra91LsVt6xXv_cdNQrHknqhyLw91MUm1TErf06dZPnV42Y.; SUB=_2A25MQSB3DeRhGeVJ41AX-S3JwjyIHXVvNxa_rDV8PUNbmtAKLWTmkW9NT8Y82JrjRBaDX-xHbT26W1vPOq-XfSVU; XSRF-TOKEN=JBW39814_JwIP3jQm5LEk2Gf; WBPSESS=eos1U0TOL9RQWkwSB_5XloC2SO_sW1NfyVQvv8fyd4Et9zsX3wOrX2LgsZ1kMiaoUjBzFb-61qLIkVnnUtRYyqllq3ky0BAtllhRHFClfP2J8aiIqlsFw449u8wd_4C9; _s_tentry=www.baidu.com; UOR=account.autohome.com.cn,widget.weibo.com,www.baidu.com; Apache=7700581050586.907.1631934102866; ULV=1631934102871:14:1:1:7700581050586.907.1631934102866:1627100183216',
    'referer':'https://weibo.com/'
}
request=urllib.request.Request(url=url,headers=header)
response=urllib.request.urlopen(request)
content=response.read().decode('utf-8')

with open('weibo.html','w',encoding='utf-8') as fp :
    fp.write(content)
# print('content')