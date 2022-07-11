import urllib.request
from lxml import etree
# https://sc.chinaz.com/tupian/xingganmeinvtupian.html
# User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4595.0 Safari/537.36
# GET
# url='https://sc.chinaz.com/tupian/xingganmeinvtupian.html'
# https://sc.chinaz.com/tupian/xingganmeinvtupian_2.html
# headers={
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4595.0 Safari/537.36'
# }
# 请求对象的定制
def creat_request(page) :
    headers={
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4595.0 Safari/537.36'
    }
    if page==1 :
        url='https://sc.chinaz.com/tupian/xingganmeinvtupian.html'
        request=urllib.request.Request(url=url,headers=headers)
        return request
    else :
        url='https://sc.chinaz.com/tupian/xingganmeinvtupian_'+str(page)+'.html'
        request=urllib.request.Request(url=url,headers=headers)
        return request

# 响应服务器数据
def get_content(request) :
    response=urllib.request.urlopen(request)
    content=response.read().decode('utf-8')
    return content

# 下载图片
def down_load(content) :
    # with open('站长素材第'+str(page)+'.json','w',encoding='utf-8') as fp :
        # 响应服务器的数据 解析它
        # urllib.request.urlretrieve("图片地址","文件名字")

        tree=etree.HTML(content)    #解析数据
        # 服务器的懒加载  这个不能写src 要去页面找到真正的'src',这里是src2
        # 这个是图片的名字      '//div[@id="container"]//a/img/@alt'
        # result=tree.xpath('//div[@id="container"]//a/img/@src')

        name_list=tree.xpath('//div[@id="container"]//a/img/@alt') #获取的是列表的格式 需要转化 这里不能用int()，因为它是列表
        # 但是可以用 range(len(name_list))
        src_list=tree.xpath('//div[@id="container"]//a/img/@src2')
        # print(len(src_list))
        for i in range(len(name_list)):
            name=name_list[i]
            # 采用切片 使得去掉最后的 _S.jpg从而获取到 原图的效果 (不能写png,格式要一致)
            src=src_list[i][:-6]+".jpg"
            url='https:'+src
            # print(name,url)
            print(name,'爬取成功！！！')
            urllib.request.urlretrieve(url=url,filename='./img/'+name+'.jpg')

# 请求对象的定制
# request=urllib.request.Request(url=url,headers=headers)
# 响应服务器请求
# response=urllib.request.urlopen(request)
# print(response)
# content=response.read().decode('utf-8')
# print(content)

if  __name__=='__main__' :
    start_page=int(input("请输入开始页码"))
    end_page=int(input("请输入结束页码"))
    for page in range(start_page,end_page+1) :
        # 要加range  如果只写了括号  是元组类型
        request=creat_request(page)
        # print(request)
        content=get_content(request)
        # print(content)
        down_load(content)

