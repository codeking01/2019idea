'''
@author king_xiong
@date 2022-03-06 9:42
'''
import json
import time

import requests
from lxml import etree
from selenium import webdriver


def get_content(url, headers, ):
    '''
    # 获取页面内容
    :return:
    '''
    content = requests.get(url=url, headers=headers, timeout=10).text
    # print(content)
    tree = etree.HTML(content)
    context = tree.xpath('//*[@id="ibu-hotel-detail-head"]/div[1]/div[1]/div[2]/div[2]/span[2]/text()')
    print(context)


if __name__ == '__main__':
    # url = 'https://hotels.ctrip.com/hotels/detail/?hotelId=42702623&checkIn=2022-03-06&checkOut=2022-03-07&cityId=206&minprice=&mincurr=&adult=1&children=0&ages=&crn=1&curr=&fgt=&stand=&stdcode=&hpaopts=&mproom=&ouid=&shoppingid=&roomkey=&highprice=-1&lowprice=0&showtotalamt=&hotelUniqueKey='
    url = 'https://www.ctrip.com/'
    # 首页地址 https://hotels.ctrip.com/hotels/list?countryId=1&city=206&highPrice=-1&barCurr=CNY&location=483&sort=1&category=eyJmaWx0ZXJJZCI6Ijc1fFRBR180ODkiLCJ0eXBlIjoiNzUiLCJ2YWx1ZSI6IjQ4OSIsInN1YlR5cGUiOiIyIiwiY2hpbGRWYWx1ZSI6IiIsInByb3BlcnR5VmFsdWUiOiIifQ%3D%3D
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.128 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'Accept-Language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7',
        'Upgrade-Insecure-Requests': '1',
        'Cache-Control': 'max-age=0',
    }
    # get_content(url, headers)
    # 创建浏览器对象
    path = 'chromedriver.exe'
    browser = webdriver.Chrome(path)
    browser.get(url)
    # time.sleep(20)     # 进行扫码
    # dictCookies = browser.get_cookies()    # 获取list的cookies
    # jsonCookies = json.dumps(dictCookies) #  转换成字符串保存
    #
    # with open('damai_cookies.txt', 'w') as f:
    #     f.write(jsonCookies)
    # print('cookies保存成功！')
    # """
    # 从本地读取cookies并刷新页面,成为已登录状态
    # """
    # with open('damai_cookies.txt', 'r', encoding='utf8') as f:
    #     listCookies = json.loads(f.read())
    # # 往browser里添加cookies
    # for cookie in listCookies:
    #     cookie_dict = {
    #         'domain': '.ctrip.com',
    #         'name': cookie.get('name'),
    #         'value': cookie.get('value'),
    #         "expires": '',
    #         'path': '/',
    #         'httpOnly': False,
    #         'HostOnly': False,
    #         'Secure': False
    #     }
    #     browser.add_cookie(cookie_dict)
    # browser.refresh()


