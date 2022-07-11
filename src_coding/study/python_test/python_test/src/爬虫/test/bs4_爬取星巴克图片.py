# 图片地址： 'https://www.starbucks.com.cn/'+//ul[@class="grid padded-3 product"]//a/@href   **/images/caffe-verona-coffee-beans.png
# 图片名字 soup.select('strong')
import random
import urllib.request

from bs4 import BeautifulSoup


def create_request(url, headers):
    request = urllib.request.Request(url=url, headers=headers)
    return request

def get_content(request,opener):
    response=opener.open(request)
    content=response.read().decode('utf-8')
    return content


if __name__ == "__main__":
    url = 'https://www.starbucks.com.cn/menu/'
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4595.0 Safari/537.36'
    }
    # 加入代理
    proxies_pool = [
        {'http': '112.195.241.83: 3256'},
        {'http': '117.94.222.222: 3256'},
        {'http': '117.94.222.28	: 3256'}
    ]
    # 获取opener对象
    proxies=random.choice(proxies_pool)
    handler=urllib.request.ProxyHandler(proxies=proxies)
    opener=urllib.request.build_opener(handler)
    # 定制对象
    request = create_request(url, headers)
    # 获取响应数据内容
    content = get_content(request, opener)
    soup=BeautifulSoup(content,'lxml')
    # print(soup)
    #获取名字对象列表
    name_list=soup.select('strong')
    # 转化成文本形式
    k=0
    for i in name_list:
        name_list[k]=i.get_text()
        k+=1
        # print(name_list)
        # 这个只能获取对象
        src_list=soup.select('ul[class="grid padded-3 product"] a[href]') #'ul[class="grid padded-3 product"] a[href]'
        # print(src_list)
        # 所有的名字获取成功，存在name_list里面

        # *****
        # 下面要修改为 x，因为上面的k已经发生变化了
        # 把链接的格式找出来
    # 重置一下k,让其重新遍历
    k=0
    for i in src_list:
        # soup.a.attrs['href']
        src_list[k]='https://www.starbucks.com.cn/'+i.attrs['href']
        url=src_list[k]
        # print(url)
        request=create_request(url,headers)
        content=get_content(request,opener)
        soup=BeautifulSoup(content,'lxml')
        # # # 跳转链接以后的图片地址 //div//section/div//img[@class="product"]/@src 这个只能找到对象
        src=soup.select('div section>div img[class="product"]')
        # # 找到图片中跳转后可以下载的图片
        if src :
            # 获取想要的属性值
            final_src='https://www.starbucks.com.cn/'+src[0].attrs['src']
            # print(final_src)
            print(name_list[k], '***开始爬取.......')
            urllib.request.urlretrieve(url=final_src,filename='./pic/'+str(k)+'.jpg')
            print(name_list[k])

            print('第{0}条数据处理成功'.format(k))
        k+=1    #继续遍历这个列表


        # # print(src_list)
