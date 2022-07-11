# 下载内容的方法 urllib.request.urlretrieve(url=src，filename=filename)
# url='https://www.shicimingju.com/book/sanguoyanyi.html'
# 'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4595.0 Safari/537.36'
# 地址：//div[@id="main_left"]//ul/li/a/@href 第i回地址
# 地址补充： 这个地方注意  超链接并不全，所以在跳转以后查看新的地址，需要补全这个地址 ：'https://www.shicimingju.com/'+
# 名字：//div[@id="main_left"]//ul/li/a/text()
# //div[@id="main_left"]//h1  三国演义
#  文本内容解析：//div[@id="main"]//div[@class="card bookmark-list"]//text()

import random
import urllib.request
from lxml import etree


def create_request(url):
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4595.0 Safari/537.36'
    }
    # 定制对象
    request = urllib.request.Request(url=url, headers=headers)
    return request


def get_content(request):
    # 加代理池
    proxies_pool = [
        {'http': '112.195.241.83: 3256'},
        {'http': '117.94.222.222: 3256'},
        {'http': '117.94.222.28	: 3256'}
    ]
    proxies = random.choice(proxies_pool)
    # 加代理
    handler = urllib.request.ProxyHandler(proxies=proxies)
    opener = urllib.request.build_opener(handler)
    # 响应服务器数据
    response = opener.open(request)
    content = response.read().decode('utf-8')
    return content
    # print(content)


def get_text_content(src):
    # # 获取链接的定制对象
    href_request = create_request(src)
    # # 响应服务器数据（获取内容）
    href_content = get_content(href_request)
    # print(href_content)
    # 章节内容 ：'//div[@id="main"]//div[@class="card bookmark-list"]//text()'
    # 注意这个地方  tree要重新命名，前面有一个tree了
    href_tree = etree.HTML(href_content)
    # print(new_tree)
    # # 接收文本内容
    text_content = href_tree.xpath('//div[@id="main"]//div[@class="card bookmark-list"]//text()')
    # 需要分奇数页和偶数页(不用也可以)

    ####
    # text_content = str(text_content) #这个转化字符串的 依旧是是一个列表形式
    # print(type(text_content))
    text_content = [str(i) for i in text_content]
    final_content = ''.join(text_content)  # 转化为一个长的字符串
    return final_content
    # print(type(final_content),final_content)

    # 这个测试不对 urllib.request.urlretrieve(url=src, filename="./text/" + name_list[i] + ".text")


if __name__ == '__main__':
    # k = 0 #测试用的
    # 主页地址
    url = 'https://www.shicimingju.com/book/sanguoyanyi.html'
    request = create_request(url)
    content = get_content(request)
    # 解析数据
    tree = etree.HTML(content)
    # 章节名字存到name_list
    name_list = tree.xpath('//div[@id="main_left"]//ul/li/a/text()')

    for i in range(len(name_list)):
        # if  k== 2:
        #     exit(0)
        # else:
        try:
            # k += 1
            name = name_list[i]
            src = 'https://www.shicimingju.com/' + tree.xpath('//div[@id="main_left"]//ul/li/a/@href')[i]
            # print(name,src)

            # 获取文本内容
            final_content = get_text_content(src)

            # 写到文件中（注意新建一个text的文件，这样下载的东西就不会很乱了）
            with open('./text/' + '三国' + str(name_list[i] + '.'), 'w', encoding='utf-8') as fp:
                fp.write(final_content)
            print(name, '爬取成功！！！')

        except:
            print('第{0}条数据处理失败'.format(i))
