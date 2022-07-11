from selenium import webdriver
import time

# 获取browser对象
path = 'chromedriver.exe'
browser = webdriver.Chrome(path)

# 模拟用浏览器打开 这个url
url = 'https://www.baidu.com/'
browser.get(url)
time.sleep(2)
# 获取相应的元素---*获取文本框
input = browser.find_element_by_id('kw')

input.send_keys('百度一下')
time.sleep(1)

# 获取百度一下的按钮
button = browser.find_element_by_xpath('//div//input[@id="su"]')
button.click()
time.sleep(1)
# 模拟JS滚动:
js='document.documentElement.scrollTop=100000'
browser.execute_script(js) #执行js代码
time.sleep(2)

# 获取点击下一页按钮
next_button=browser.find_element_by_xpath('//a[@class="n"]')
next_button.click()
time.sleep(2)

# 回到上一级操作
browser.back()
time.sleep(1)
# 在往前操作一步
browser.forward()


