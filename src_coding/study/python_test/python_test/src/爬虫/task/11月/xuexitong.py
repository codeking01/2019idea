import time
from lxml import etree

import requests
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.options import Options
import requests

def share_browser():
    chrome_options = Options()
    chrome_options.add_argument('‐‐headless')
    chrome_options.add_argument('‐‐disable‐gpu')
    path = r'C:\Program Files (x86)\Google\Chrome\Application\chrome.exe'
    chrome_options.binary_location = path
    browser = webdriver.Chrome(chrome_options=chrome_options)
    return browser
browser=share_browser()
# session=requests.session()
# post_data = {'username':'','password':''}
# url='http://office.chaoxing.com/front/web/apps/forms/fore/apply?uid=69761895&code=smXOjH3Q&mappId=5300924&appId=3c9c9642139643ba91477f442d69becc&appKey=l2E6J3d1g0B%2F5bCG&id=14788&enc=06fbc4bd4c56c44afabca4103d961275'
# headers={
#     'Cookie':'search_uuid=29d9afc1%2d6820%2d4ffe%2d8eb1%2d3d731b5f82ff; lv=2; fid=3208; _uid=56883925; uf=94ffe74515793f362ce45560cdcab25327f5bf23d95da52963355f172239022bcea4520279fe5d222c65b42cbb44d2aac49d67c0c30ca5047c5a963e85f11099df75aa2875b1816bfd68be96b6183b1a15ba01ec738f02a6a008d84d6b3f7e1e05f7adb0b9cd865a; _d=1636097954017; UID=56883925; vc=1C8547C99BE641FE2368EFF44B3D1E5E; vc2=7D6794CD0163F9F8220B91ED3AE2655A; vc3=YAy45KQfBanwNOERrr902UOly%2BVppW6T9i828va0WUKl9E9xvsE4kk%2Fy9UzGE78PKJsVUfJQlfqyNXE4Wqd8fo6mTk5Jlry5BvzHN%2BgyNybf55%2F4YdGrNKpOeDQc%2B0bOBDny5%2Fs3RK%2FPemxc7KfSdOeLtwoxeqtIjIOhuduj63U%3Ddc643cd2419a23499197379635097c35; xxtenc=e4b27a1a10e47d3fe4e70b55edf6e167; DSSTASH_LOG=C_38-UN_2149-US_56883925-T_1636097954019; JSESSIONID=89C9A6FBA89E4EAB81AEEB8D934816D9.oaapp_web_24_9; oa_deptid=3208; oa_uid=56883925; oa_name=%E7%86%8A%E5%98%89%E4%BA%AE; oa_enc=ae0f3ed4a401da7b85961c2971f9abb4; route=24b68763a0e084beec86cc31ab344491',
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36',
# }
# res = session.post(url=url,data=post_data,headers=headers)	#　登陆
# print(res)
# browser.add_cookie('_lxsdk_cuid=17c7f907122c8-005a3d1714b78c-b7a1438-144000-17c7f907122c8; _lxsdk=17c7f907122c8-005a3d1714b78c-b7a1438-144000-17c7f907122c8; _hc.v=751dd7ad-f61c-e41b-0401-95d1866ae493.1634227745; s_ViewType=10; ctu=1dc952f673738fa47d20413160405840235920484dc849760c4a66b318dd0f6b; fspop=test; ua=sunshine; dper=234cb94f92704aef13a7e6c816ada0ec99322848b9a103cfe3bd94b17b5973abe3504b1c18ec4575f82a7f8e19bc2765a23a9a9541ab953eeca862f3c2712be82cce25199a025ec99a3cb8500c39eae6f33a8983370d8fb82c9739611bd81246; ll=7fd06e815b796be3df069dec7836c3df; Hm_lvt_602b80cf8079ae6591966cc70a3940e7=1635434475,1635479818,1635574037,1635611895; cye=shanghai; cy=1; dplet=d34cef477d103bc73ac23b9303221b73; _lxsdk_s=17cd192f0f0-4b9-470-d78%7C%7C838; Hm_lpvt_602b80cf8079ae6591966cc70a3940e7=1635614493')
# browser.add_cookie('search_uuid=29d9afc1%2d6820%2d4ffe%2d8eb1%2d3d731b5f82ff; lv=2; fid=3208; _uid=56883925; uf=94ffe74515793f362ce45560cdcab25327f5bf23d95da52963355f172239022bcea4520279fe5d222c65b42cbb44d2aac49d67c0c30ca5047c5a963e85f11099df75aa2875b1816bfd68be96b6183b1a15ba01ec738f02a6a008d84d6b3f7e1e05f7adb0b9cd865a; _d=1636097954017; UID=56883925; vc=1C8547C99BE641FE2368EFF44B3D1E5E; vc2=7D6794CD0163F9F8220B91ED3AE2655A; vc3=YAy45KQfBanwNOERrr902UOly%2BVppW6T9i828va0WUKl9E9xvsE4kk%2Fy9UzGE78PKJsVUfJQlfqyNXE4Wqd8fo6mTk5Jlry5BvzHN%2BgyNybf55%2F4YdGrNKpOeDQc%2B0bOBDny5%2Fs3RK%2FPemxc7KfSdOeLtwoxeqtIjIOhuduj63U%3Ddc643cd2419a23499197379635097c35; xxtenc=e4b27a1a10e47d3fe4e70b55edf6e167; DSSTASH_LOG=C_38-UN_2149-US_56883925-T_1636097954019; JSESSIONID=89C9A6FBA89E4EAB81AEEB8D934816D9.oaapp_web_24_9; oa_deptid=3208; oa_uid=56883925; oa_name=%E7%86%8A%E5%98%89%E4%BA%AE; oa_enc=ae0f3ed4a401da7b85961c2971f9abb4; route=24b68763a0e084beec86cc31ab344491')
browser.get('http://office.chaoxing.com/front/web/apps/forms/fore/apply?uid=69761895&code=smXOjH3Q&mappId=5300924&appId=3c9c9642139643ba91477f442d69becc&appKey=l2E6J3d1g0B%2F5bCG&id=14788&enc=06fbc4bd4c56c44afabca4103d961275')
input_name=browser.find_element_by_xpath('//input[@class="ipt-tel"]')
input_name.send_keys('15630138378')
input_password=browser.find_element_by_xpath('//input[@class="ipt-pwd"]')
input_password.send_keys('990416AA')
login_button=browser.find_element_by_xpath('//button').click()
time.sleep(3)
print(browser.page_source)
element=browser.find_element_by_xpath('//input')
print(element)
# print(element.text)
# print(tip.click())
# element.click()
time.sleep(3)
browser.quit()

# input_temp1=browser.find_element_by_xpath('//input[@class="inputM error"]')
# time.sleep(5)
# res=browser.page_source
# print(type(res))
# print(res)
# tree=etree.HMTL(res)

# win = browser.switch_to.alert
# win.accept()
# alert = browser.switch_to.alert
# search_window = browser.current_window_handle
# input_tmp1=browser.find_element_by_xpath('//input[@class="inputM"]')
# alert.accept()
# input_tmp1.send_keys('36.5')

# browser.switch_to.window(browser.window_handles[0])
# a=browser.find_element_by_xpath('//input[@class="inputM error"]')
# print(a)