import mitmproxy
import traceback
from mitmproxy import ctx,http
from mitmproxy.http import flow
from bs4 import BeautifulSoup as BS


def parse_shop(html):
    shop_info = []
    soup = BS(html, 'lxml')
    page_shop = soup.find_all('div', class_='txt')
    for shop in page_shop:
        shop_info.append({
            'shopid': shop.a['data-shopid'],
            'name': shop.a.text.strip(),
            'score': shop.find('div', class_='nebula_star').text.strip()
        })
    return shop_info


def parse_comment(html):
    soup = BS(html, 'lxml')
    comments = soup.find_all('div', class_='main-review')
    comment_list = []
    for item in comments:   # 遍历所有评论
        username = item.find('div', class_='dper-info').text.strip()
        items = item.find_all('span', class_='item')     # 各项评分
        detail_score = []
        for _item in items:
            detail_score.append(_item.text.strip())
        content = item.find('div', class_='review-words').text.strip()  # 获取到的评论不全，做了CSS加密
        comment_list.append({'username': username, 'item': detail_score, 'content': content})
    return comment_list


class Spider:
    def response(self, flow:flow):
        # 去掉cookie的HttpOnly参数
        shop_list_url = 'http://www.dianping.com/guangzhou'

        url = flow.request.url
        if url.startswith(shop_list_url):
            print(f'mitm 劫持成功,URL= {url}')
            # headers = flow.request.headers
            body = flow.response.text
            shop_info = parse_shop(body)
            for _ in shop_info:
                print(_)
        elif 'review_all' in url and url.startswith('http://www.dianping.com'):
            print(f'mitm 劫持成功,URL= {url}')
            # headers = flow.request.headers
            body = flow.response.text
            comment_list = parse_comment(body)
            for _ in comment_list:
                print(_)
                print(20*'--')


addons = [
    Spider(),
]