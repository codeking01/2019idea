from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

def share_browser():
    chrome_options = Options()
    chrome_options.add_argument('‐‐headless')
    chrome_options.add_argument('‐‐disable‐gpu')
    path = r'C:\Program Files (x86)\Google\Chrome\Application\chrome.exe'
    chrome_options.binary_location = path
    browser = webdriver.Chrome(chrome_options=chrome_options)
    return browser
time.sleep(2)
browser=share_browser()
browser.get('https://passport2.chaoxing.com/login')
# input=browser.find_element_by_id('kw')
# input.send_keys("学习通")
time.sleep(2)

name_input=browser.find_element_by_xpath('//td/input[@class="zl_input"]')
name_input.send_keys('15630138378')
time.sleep(2)
password_input=browser.find_element_by_xpath('zl_input2')
password_input.send_keys('990416AA')

# button=browser.find_element_by_xpath('//span[@id="s_btn_wr"]/input')
# button.click()
# http://passport2.chaoxing.com/login?fid=&newversion=true&refer=http%3A%2F%2Fi.chaoxing.com
# href_button=browser.find_element_by_xpath('//h3[@class="t"]/a')
# href_button=href_button.get_attribute('href')
# print(href_button)
