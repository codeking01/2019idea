# https://sc.chinaz.com/tupian/meinvxiezhen.html 首页
# https://sc.chinaz.com/tupian/meinvxiezhen_2.html 第2页
# User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4595.0 Safari/537.36
# 图片名字  '//div[@id="container"]//a/@alt'
# 图片地址'//div[@id="container"]//a/img/@src2'  可拼接
import urllib.request
from lxml import etree

def create_request(page):
    headers={
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4595.0 Safari/537.36'
    }
    if page==1:
        url='https://sc.chinaz.com/tupian/meinvxiezhen.html'
    else :
        url='https://sc.chinaz.com/tupian/meinvxiezhen_'+str(page)+'.html'
    request=urllib.request.Request(url=url,headers=headers)
    return request

def get_content(request) :
    response=urllib.request.urlopen(request)
    content=response.read().decode('utf-8')
    return content

def down_load(content):
    # 解析数据
    tree=etree.HTML(content)
    # 解析想要的指定的内容
    name_list=tree.xpath('//div[@id="container"]//a/img/@alt')
    pic_list=tree.xpath('//div[@id="container"]//a/img/@src2')
    # print(pic_list)
    for i in range(len(name_list)) :
        try :
            src='https:'+pic_list[i][:-6]+'.jpg'
            # print(src)
            # urllib.request.urlretrieve("图片地址","文件名字")
            urllib.request.urlretrieve(url=src,filename="./img/"+name_list[i]+".jpg")
        except:
            print('第{0}条数据处理失败'.format(i))

if __name__ == '__main__':
    start_page = (int(input("请输入起始页码")))
    end_page = (int(input("请输入结束页码")))
    for page in range(start_page, end_page+1):
#       获取定制对象
        request=create_request(page)
        # print(request)
        # 响应服务器数据
        content=get_content(request)
        # print(content)
        # 解析数据，并且下载
        down_load(content)