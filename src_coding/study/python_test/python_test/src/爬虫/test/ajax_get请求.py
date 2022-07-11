import urllib.request

# 这个是get请求的
# 所以可以进行拼接
url = 'https://movie.douban.com/j/chart/top_list?type=5&interval_id=100%3A90&action=&start=0&limit=20'
header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4595.0 Safari/537.36',
    'Cookie': 'douban-fav-remind=1; __gads=ID=b00d3847caa6bf74-22e5b58b0eca0065:T=1625213219:RT=1625213219:S=ALNI_MaIyFgcjZJwaJX5q55PYBtzhe1gaA; ll="108289"; bid=ZhXgZf19D5Q; _vwo_uuid_v2=D2BF3DD5DA23940A4431332EA261C6100|73a04c7c322338493187b1f40d163755; _pk_ref.100001.4cf6=%5B%22%22%2C%22%22%2C1631877149%2C%22https%3A%2F%2Fwww.baidu.com%2Flink%3Furl%3DuhUz3HNRD-tapj5QRPW9MAMAKWIGwMJtC3NiB_0T4itSp2OXMbtyKPKRukBONz2f%26wd%3D%26eqid%3Dd136c8c00011f9fe0000000261447818%22%5D; _pk_ses.100001.4cf6=*; ap_v=0,6.0; __utma=30149280.337626959.1564290877.1631803131.1631877149.12; __utmb=30149280.0.10.1631877149; __utmc=30149280; __utmz=30149280.1631877149.12.3.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; __utma=223695111.1062514155.1564290877.1631803135.1631877149.6; __utmb=223695111.0.10.1631877149; __utmc=223695111; __utmz=223695111.1631877149.6.2.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; _pk_id.100001.4cf6=c099aca48aa1e97e.1564290877.5.1631877172.1631803377.'
}

#定制对象  注意定制的Request里面传参的 只能是headers
request=urllib.request.Request(url=url,headers=header)
#模拟服务器发送请求
response=urllib.request.urlopen(request)
# print(response)

# 响应数据
content=response.read().decode('utf-8')
print(content)
#写入文件中
with open('douban.json','w',encoding='utf-8') as fp :
    fp.write(content)