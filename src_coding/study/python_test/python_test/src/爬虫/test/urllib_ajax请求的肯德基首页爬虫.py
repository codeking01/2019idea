import urllib.request
import urllib.parse

# http://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx?op=keyword
# POST请求
# 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4595.0 Safari/537.36'

# 定制对象
def creat_request(page) :
    url='http://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx?op=keyword'
    data={
        'cname':'',
        'pid':'',
        'keyword': '天津',
        'pageIndex': page,
        'pageSize': '10'
    }
    header={
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4595.0 Safari/537.36'
    }

    # 这个地方是post请求，那么data的数据必须编译 在编码
    data=urllib.parse.urlencode(data).encode('utf-8')
    request=urllib.request.Request(url=url,data=data,headers=header)
    return request

# 获取响应
def get_content(request) :
    response=urllib.request.urlopen(request)
    content=response.read().decode('utf-8')
    return content

# 下载数据
import json
def download(page,content):
    # 注意这个地方  不要写成
    # obj=str(json.loads(content))
    # 这样的话写入的东西 将全都是单引号 直接读取 content写入就没有问题
    with open('肯德基第'+str(page)+'页.json','w',encoding='utf-8') as fp :
        fp.write(content)
    # print(obj)

if __name__=='__main__':
    start_page=int((input("请输入起始页码")))
    end_page=int((input("请输入结束页码")))
    for page in range(start_page,end_page+1) :
        request=creat_request(page)
        # print(request)
        content=get_content(request)
        # print(content)
        download(page,content)