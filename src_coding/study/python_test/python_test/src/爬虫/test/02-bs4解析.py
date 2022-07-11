# 开发时间：2021/9/21   16:01

import requests
from bs4 import BeautifulSoup
# from fake_useragent import UserAgent

if __name__ == '__main__':
    k = 0
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4595.0 Safari/537.36',
    }
    url = 'https://www.shicimingju.com/book/sanguoyanyi.html'
    # page_text = requests.get(url=url, headers=headers).content
    page_content = requests.get(url=url, headers=headers).content

    page_text = str(page_content, 'utf-8')
    print(page_text)

    # print(page_text)
    # 在首页中解析出章节的标题和详情页的url
    # 1.实例化BeautifulSoup对象，需要将页面源码数据加载到该对象中
    soup = BeautifulSoup(page_text, 'lxml')  # lxmml解析器
    # 解析章节标题和详情页的url
    li_list = soup.select('.book-mulu > ul >li')  # 层级选择器
    fp = open('./sanguo.txt', 'w', encoding='utf-8')
    for li in li_list:
        k += 1
        title = li.a.string
        detail_url = 'https://www.shicimingju.com' + li.a['href']
        # 对详情页发起请求，解析章节内容
        detail_page_text = requests.get(url=detail_url, headers=headers).text
        # 解析出详情页的章节内容
        detail_soup = BeautifulSoup(detail_page_text, 'lxml')
        div_tag = detail_soup.find('div', class_='chapter_content')
        # 解析到章节内容
        content = div_tag.text

        fp.write(title + ':' + content + '\n')
        print(title, '爬取成功！！！')
        if k == 5:
            break
