import time
import requests
from selenium import webdriver
from bs4 import BeautifulSoup

# 登录接口 https://so.gushiwen.cn/user/login.aspx?from=http%3a%2f%2fso.gushiwen.cn%2fuser%2fcollect.aspx
url = 'https://so.gushiwen.cn/user/login.aspx?from=http%3a%2f%2fso.gushiwen.cn%2fuser%2fcollect.aspx'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36'
}
response = requests.get(url, headers=headers)
content = response.text

soup = BeautifulSoup(content, 'lxml')
# print(soup)
viewstate = soup.select('#__VIEWSTATE')[0].attrs.get('value')
viewstategenerator = soup.select('#__VIEWSTATEGENERATOR')[0].attrs.get('value')
code_url = 'https://so.gushiwen.cn' + soup.select('#imgCode')[0].attrs.get('src')

# 获取验证码
session = requests.session()
src_url = session.get(code_url)
code_content = src_url.content
with open('a.jpg', 'wb') as fp:
    fp.write(code_content)

# coding:utf-8
# !/usr/bin/env python
from hashlib import md5

def get_codename():
    class Chaojiying_Client(object):

        def __init__(self, username, password, soft_id):
            self.username = username
            password = password.encode('utf8')
            self.password = md5(password).hexdigest()
            self.soft_id = soft_id
            self.base_params = {
                'user': self.username,
                'pass2': self.password,
                'softid': self.soft_id,
            }
            self.headers = {
                'Connection': 'Keep-Alive',
                'User-Agent': 'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0)',
            }

        def PostPic(self, im, codetype):
            """
            im: 图片字节
            codetype: 题目类型 参考 http://www.chaojiying.com/price.html
            """
            params = {
                'codetype': codetype,
            }
            params.update(self.base_params)
            files = {'userfile': ('ccc.jpg', im)}
            r = requests.post('http://upload.chaojiying.net/Upload/Processing.php', data=params, files=files,
                              headers=self.headers)
            return r.json()

        def ReportError(self, im_id):
            """
            im_id:报错题目的图片ID
            """
            params = {
                'id': im_id,
            }
            params.update(self.base_params)
            r = requests.post('http://upload.chaojiying.net/Upload/ReportError.php', data=params, headers=self.headers)
            return r.json()

    if __name__ == '__main__':
        chaojiying = Chaojiying_Client('action', 'action', '922886')  # 用户中心>>软件ID 生成一个替换 96001
        im = open('a.jpg', 'rb').read()  # 本地图片文件路径 来替换 a.jpg 有时WIN系统须要//
        code_name = chaojiying.PostPic(im, 1902).get('pic_str')  # 1902 验证码类型  官方网站>>价格体系 3.4+版 print 后要加()
        return code_name


# code_name = input('请输入你的验证码')
code_name=get_codename()
# print(code_name)



# 点击登陆
url_post = 'https://so.gushiwen.cn/user/login.aspx?from=http%3a%2f%2fso.gushiwen.cn%2fuser%2fcollect.aspx'

data_post = {
    '__VIEWSTATE': viewstate,
    '__VIEWSTATEGENERATOR': viewstategenerator,
    'from': 'http://so.gushiwen.cn/user/collect.aspx',
    'email': '595165358@qq.com',
    'pwd': 'action',
    'code': code_name,
    'denglu': '登录',
}

response_post = session.post(url=url_post, headers=headers, data=data_post)

content_post = response_post.text

with open('gushiwen.html', 'w', encoding='utf-8')as fp:
    fp.write(content_post)

# # 模拟一个浏览器去访问
# path='chromedriver.exe'
# browser=webdriver.Chrome(path)
# browser.get(session.post(url=url_post, headers=headers, data=data_post))