'''
@author king_xiong
@date 2021-12-19 0:08
'''
from selenium import webdriver
#这个是浏览器自带的 不需要我们再做额外的操作
from selenium.webdriver.chrome.options import Options
def share_browser():
    #初始化
    chrome_options = Options()
    chrome_options.add_argument('‐‐headless')
    chrome_options.add_argument('‐‐disable‐gpu')
    #浏览器的安装路径 打开文件位置
    #这个路径是你谷歌浏览器的路径
    path = r'C:\Program Files\Google\Chrome\Application\chrome.exe'
    chrome_options.binary_location = path
    browser = webdriver.Chrome(chrome_options=chrome_options)
    return browser
# 封装调用：

browser = share_browser()
browser.get('http://www.baidu.com/')