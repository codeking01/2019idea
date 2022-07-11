import time
import urllib.request
from selenium import webdriver


headers={
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.54 Safari/537.36'
}
# 导入这个phantom.js 无界面浏览器插件
path='phantomjs.exe'
browser=webdriver.PhantomJS(path)

# 输入想要爬取的网址
url='https://www.jd.com/'
browser.get(url)
# print(url)
request=urllib.request.Request(url=url,headers=headers)
response=urllib.request.urlopen(request)
content=response.read().decode('utf-8')
# 保存快照
# browser.save_screenshot('jd.png')
time.sleep(2)
# print(content)
button=browser.find_element_by_xpath('//div[@class="form"]//input')
button.click()
# print(button)
time.sleep(6)
browser.save_screenshot('秒杀.png')


