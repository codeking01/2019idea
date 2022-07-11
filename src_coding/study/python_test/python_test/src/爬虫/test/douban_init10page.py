import urllib.request
import urllib.parse

# https://movie.douban.com/j/chart/top_list?type=5&interval_id=100%3A90&action=&
# start=40&limit=20
# 这个是get 请求

def creat_request(page) :
    header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4595.0 Safari/537.36'
    }
    data={
        'start':(page-1)*10,
        'limit':20
    }
    data=urllib.parse.urlencode(data)
    base_url='https://movie.douban.com/j/chart/top_list?type=5&interval_id=100%3A90&action=&'
    url=base_url+data
    # 定制对象
    request=urllib.request.Request(url=url,headers=header)
    return request

def get_content(request):
    response=urllib.request.urlopen(request)
    content=response.read().decode('utf-8')
    return content

def download(page,content):
    with open('douban'+str(page)+'.json','w',encoding='utf-8') as fp:
        fp.write(content)
    # return content

if __name__=='__main__':
    start_page=int(input("请输入开始页码"))
    end_page=int(input("请输入结束页码"))
    for page in range(start_page,end_page+1) :
        request=creat_request(page)
        print(request)
        #模拟服务器发送请求
        # response=urllib.request.urlopen(request) 写在新方法 get_content里面
        # print(response)
        # 响应服务器数据
        content=get_content(request)
        # print(content)
        download(page,content)