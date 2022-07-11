# 网页地址https://landing.zhaopin.com/resume-templates
# 图片链接 //div[@class="a-center-layout"]//div/a/@href
# 图片地址 //div[@id="root"]//div//img[@class="template-preview__main-image"]/@src
import random
import urllib.request
from lxml import etree


def create_request(url,headers):
    request = urllib.request.Request(url=url,headers=headers)
    return request

def get_content(request,opener):
    response = opener.open(request)
    content = response.read().decode('utf-8')
    return content


if __name__ == '__main__':
    k=0
    url = 'https://landing.zhaopin.com/resume-templates'
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4595.0 Safari/537.36'
    }
    proxies_pool = [
        {'http': '112.195.241.83: 3256'},
        {'http': '117.94.222.222: 3256'},
        {'http': '117.94.222.28	: 3256'}
    ]
    # 加代理
    proxies = random.choice(proxies_pool)
    handler=urllib.request.ProxyHandler(proxies=proxies)
    opener=urllib.request.build_opener(handler)
    # 定制对象
    request=create_request(url,headers)

    # 响应服务器数据
    content=get_content(request,opener)


    # 解析数据
    tree = etree.HTML(content)
    src_list = tree.xpath('//div[@class="a-center-layout"]//div/a/@href')
    # print(src_list)

    # 地址补全 'https://landing.zhaopin.com/'
    for i in src_list:
        k+=1
        # print('https://landing.zhaopin.com/'+i)
        url='https://landing.zhaopin.com/'+i #每个链接的地址
        request=create_request(url,headers)#定制对象
        content=get_content(request,opener)#获取内容
        src_tree = etree.HTML(content)
        # 下面这个是列表类型的
        src = src_tree.xpath('//div[@id="root"]//div//img[@class="template-preview__main-image"]/@src')
        tran_src=src[0].split("?")[0] #list类型的 索引 不要加 “.”
        # src=tran_src.[0]
        # print(tran_src)
        #下载到文件中
        urllib.request.urlretrieve(url=tran_src,filename='./pic/'+str(k)+'.jpg')
        print('第{0}条下载成功'.format(k))

# new_list = [str(i) for i in src_list]
# new_list=''.join(new_list)
# print(new_list)
# print(content)
