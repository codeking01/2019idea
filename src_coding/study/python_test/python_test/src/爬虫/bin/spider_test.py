import urllib.request

def getHtml(url):
    response = urllib.request.urlopen(url)
    print(type(response))
    # <class 'http.client.HTTPResponse'>
    # html = response.read().decode('utf-8')
    # 这个是按照一个字节一个字节去阅读的
    # read() 里面的（）的数字代表读取多少个字节
    # 例如 read（5） --》  得到<!DOC

    # 优化一下 一行一行读取
    html = response.readlines()
    return html

html = getHtml("http://www.baidu.com")

response=urllib.request.urlopen("http://www.baidu.com")
print(response.getcode())  #获取状态码
print(response.getheaders()) #获取状态信息
print(html)
