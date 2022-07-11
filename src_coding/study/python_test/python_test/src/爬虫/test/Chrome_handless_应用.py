import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def share_browser():
    chrome_options = Options()
    chrome_options.add_argument('‐‐headless')
    chrome_options.add_argument('‐‐disable‐gpu')
    path = r'C:\Program Files (x86)\Google\Chrome\Application\chrome.exe'
    chrome_options.binary_location = path
    browser = webdriver.Chrome(chrome_options=chrome_options)
    return browser

# 获取chrome handless 浏览器
browser=share_browser()
# browser.add_cookie('_lxsdk_cuid=17c7f907122c8-005a3d1714b78c-b7a1438-144000-17c7f907122c8; _lxsdk=17c7f907122c8-005a3d1714b78c-b7a1438-144000-17c7f907122c8; _hc.v=751dd7ad-f61c-e41b-0401-95d1866ae493.1634227745; s_ViewType=10; ctu=1dc952f673738fa47d20413160405840235920484dc849760c4a66b318dd0f6b; fspop=test; ua=sunshine; dper=234cb94f92704aef13a7e6c816ada0ec99322848b9a103cfe3bd94b17b5973abe3504b1c18ec4575f82a7f8e19bc2765a23a9a9541ab953eeca862f3c2712be82cce25199a025ec99a3cb8500c39eae6f33a8983370d8fb82c9739611bd81246; ll=7fd06e815b796be3df069dec7836c3df; Hm_lvt_602b80cf8079ae6591966cc70a3940e7=1635434475,1635479818,1635574037,1635611895; cye=shanghai; cy=1; dplet=d34cef477d103bc73ac23b9303221b73; _lxsdk_s=17cd192f0f0-4b9-470-d78%7C%7C838; Hm_lpvt_602b80cf8079ae6591966cc70a3940e7=1635614493')
browser.add_cookie('_lxsdk_cuid=17c7f907122c8-005a3d1714b78c-b7a1438-144000-17c7f907122c8; _lxsdk=17c7f907122c8-005a3d1714b78c-b7a1438-144000-17c7f907122c8; _hc.v=751dd7ad-f61c-e41b-0401-95d1866ae493.1634227745; s_ViewType=10; ctu=1dc952f673738fa47d20413160405840235920484dc849760c4a66b318dd0f6b; fspop=test; cy=344; cye=changsha; ua=sunshine; aburl=1; Hm_lvt_dbeeb675516927da776beeb1d9802bd4=1635694823; Hm_lvt_4c4fc10949f0d691f3a2cc4ca5065397=1635694848; thirdtoken=6a05af06-b1c5-4209-a461-ced6ac93f235; dper=234cb94f92704aef13a7e6c816ada0ecb5011e04b4651236fa7da3788d054aa5ba1ee6237065118393683a6ad5ff779c62fda759e8e4b3c1c477c0356d455deb912f45b00884023b74ee0c07f629508b8b625aa9eeac0887107c4dc577bbf269; ll=7fd06e815b796be3df069dec7836c3df; ctu=b58a9fce079b27059480a633b27a83c8ab3d9b644f4a691fc79c19f1497f8d7386523429e0f300e831e4408919ae07c6; _lx_utm=utm_source%3DBaidu%26utm_medium%3Dorganic; Hm_lvt_602b80cf8079ae6591966cc70a3940e7=1635733253,1635734255,1635734261,1635734965; dplet=eb4919f739ecb9a851c2690531a26c8e; Hm_lpvt_602b80cf8079ae6591966cc70a3940e7=1635740879; _lxsdk_s=17cd9aad20e-c5a-c9c-3bf%7C%7C106')
# browser.get('http://www.dianping.com/shop/H7mAZatjzHao8zvm')
# text=browser.find_elements_by_xpath('')
# def getCookies():
#     url = "http://www.dianping.com/"
#     browser.get("https://account.dianping.com/login?redir=http%3A%2F%2Fwww.dianping.com%2F")
#     while True:
#         print("Please login in dianping.com!")
#         time.sleep(3)
#         while browser.current_url == url:
#             tbCookies = browser.get_cookies()
#             print(tbCookies)
#             browser.quit()
# getCookies()
# c_list=[{'domain': '.dianping.com', 'expiry': 1635732455, 'httpOnly': False, 'name': '_lxsdk_s', 'path': '/', 'secure': False, 'value': '17cd9250977-6a9-9cf-d9f%7C%7C5'}, {'domain': '.dianping.com', 'expiry': 1730338655, 'httpOnly': False, 'name': '_lxsdk', 'path': '/', 'secure': False, 'value': '17cd9250976c8-04ae893c987d61-b7a1438-144000-17cd9250977c8'}, {'domain': '.dianping.com', 'httpOnly': False, 'name': 'Hm_lpvt_602b80cf8079ae6591966cc70a3940e7', 'path': '/', 'secure': False, 'value': '1635730656'}, {'domain': '.dianping.com', 'expiry': 1667266655, 'httpOnly': False, 'name': 'Hm_lvt_602b80cf8079ae6591966cc70a3940e7', 'path': '/', 'secure': False, 'value': '1635730614'}, {'domain': '.dianping.com', 'expiry': 1730338655, 'httpOnly': False, 'name': '_lxsdk_cuid', 'path': '/', 'secure': False, 'value': '17cd9250976c8-04ae893c987d61-b7a1438-144000-17cd9250977c8'}, {'domain': '.dianping.com', 'expiry': 1636335454, 'httpOnly': False, 'name': 'fspop', 'path': '/', 'secure': False, 'value': 'test'}, {'domain': '.dianping.com', 'expiry': 1667266654, 'httpOnly': False, 'name': 'ctu', 'path': '/', 'secure': False, 'value': '1dc952f673738fa47d2041316040584045f7c0df3bc71e126aa1c65cebf052ee'}, {'domain': '.dianping.com', 'expiry': 1667266654, 'httpOnly': False, 'name': 'ua', 'path': '/', 'secure': False, 'value': 'sunshine'}, {'domain': '.dianping.com', 'httpOnly': False, 'name': 'll', 'path': '/', 'secure': False, 'value': '7fd06e815b796be3df069dec7836c3df'}, {'domain': '.dianping.com', 'expiry': 1635752254, 'httpOnly': True, 'name': 'dper', 'path': '/', 'secure': False, 'value': '234cb94f92704aef13a7e6c816ada0ec21c5227a327dadaf95f9ae0eb18ce8c227f9efaff3254497a588751b4d393e1d4952baebeb3e6532260c011179aeee21'}, {'domain': '.dianping.com', 'expiry': 1638409054, 'httpOnly': False, 'name': 'cy', 'path': '/', 'secure': False, 'value': '10'}, {'domain': '.dianping.com', 'expiry': 1667266655, 'httpOnly': False, 'name': '_hc.v', 'path': '/', 'secure': False, 'value': '0f8ea03f-394e-796e-04e2-63a4c007eb30.1635730656'}, {'domain': '.dianping.com', 'httpOnly': False, 'name': 'thirdtoken', 'path': '/', 'secure': False, 'value': '8778abd8-fa22-42ed-a45e-5fd2f48ae574'}, {'domain': '.dianping.com', 'expiry': 1638409054, 'httpOnly': False, 'name': 'cye', 'path': '/', 'secure': False, 'value': 'tianjin'}, {'domain': '.dianping.com', 'expiry': 1635752254, 'httpOnly': True, 'name': 'dplet', 'path': '/', 'secure': False, 'value': '967c2424b43dca9d67cf835398c0f4c6'}]
# # browser.get('https://account.dianping.com/login?redir=http%3A%2F%2Fwww.dianping.com%2F')
# for c in c_list:
#     browser.add_cookie({
#         "domain": ".dianping.com",
#         "name": c['name'],
#         "value": c['value'],
#         "path": '/',
#         "expires": None
#     })
browser.get('https://www.dianping.com/ajax/json/shopDynamic/reviewAndStar?shopId=k41QYj1nqhfBH70c&cityId=344&mainCategoryId=34246')
a='_lxsdk_cuid=17c7f907122c8-005a3d1714b78c-b7a1438-144000-17c7f907122c8; _lxsdk=17c7f907122c8-005a3d1714b78c-b7a1438-144000-17c7f907122c8; _hc.v=751dd7ad-f61c-e41b-0401-95d1866ae493.1634227745; s_ViewType=10; ctu=1dc952f673738fa47d20413160405840235920484dc849760c4a66b318dd0f6b; fspop=test; cy=344; cye=changsha; ua=sunshine; aburl=1; Hm_lvt_dbeeb675516927da776beeb1d9802bd4=1635694823; Hm_lvt_4c4fc10949f0d691f3a2cc4ca5065397=1635694848; _lx_utm=utm_source%3DBaidu%26utm_medium%3Dorganic; Hm_lvt_602b80cf8079ae6591966cc70a3940e7=1635693665,1635693975,1635694811,1635730214; thirdtoken=6a05af06-b1c5-4209-a461-ced6ac93f235; dper=234cb94f92704aef13a7e6c816ada0ecb5011e04b4651236fa7da3788d054aa5ba1ee6237065118393683a6ad5ff779c62fda759e8e4b3c1c477c0356d455deb912f45b00884023b74ee0c07f629508b8b625aa9eeac0887107c4dc577bbf269; ll=7fd06e815b796be3df069dec7836c3df; ctu=b58a9fce079b27059480a633b27a83c8ab3d9b644f4a691fc79c19f1497f8d7386523429e0f300e831e4408919ae07c6; dplet=5626ab06b36909493cd143828c4afa3d; Hm_lpvt_602b80cf8079ae6591966cc70a3940e7=1635731254; _lxsdk_s=17cd91e4bb8-1eb-c46-279%7C%7C129'
b='_lxsdk_cuid=17c7f907122c8-005a3d1714b78c-b7a1438-144000-17c7f907122c8; _lxsdk=17c7f907122c8-005a3d1714b78c-b7a1438-144000-17c7f907122c8; _hc.v=751dd7ad-f61c-e41b-0401-95d1866ae493.1634227745; s_ViewType=10; ctu=1dc952f673738fa47d20413160405840235920484dc849760c4a66b318dd0f6b; fspop=test; cy=344; cye=changsha; ua=sunshine; aburl=1; Hm_lvt_dbeeb675516927da776beeb1d9802bd4=1635694823; Hm_lvt_4c4fc10949f0d691f3a2cc4ca5065397=1635694848; thirdtoken=6a05af06-b1c5-4209-a461-ced6ac93f235; dper=234cb94f92704aef13a7e6c816ada0ecb5011e04b4651236fa7da3788d054aa5ba1ee6237065118393683a6ad5ff779c62fda759e8e4b3c1c477c0356d455deb912f45b00884023b74ee0c07f629508b8b625aa9eeac0887107c4dc577bbf269; ll=7fd06e815b796be3df069dec7836c3df; ctu=b58a9fce079b27059480a633b27a83c8ab3d9b644f4a691fc79c19f1497f8d7386523429e0f300e831e4408919ae07c6; _lx_utm=utm_source%3DBaidu%26utm_medium%3Dorganic; dplet=df76180a7d1b3b963c1bb8756115c462; Hm_lvt_602b80cf8079ae6591966cc70a3940e7=1635693975,1635694811,1635730214,1635732164; Hm_lpvt_602b80cf8079ae6591966cc70a3940e7=1635732164; _lxsdk_s=17cd91e4bb8-1eb-c46-279%7C%7C209'
# print(a is b)
# 从第9开始爬取


# 获取搜索框的按钮
# input=browser.find_element_by_xpath('//div[@class="form"]//input')
# # print(button)
#
# js='document.documentElement.scrollTop=100000'
# browser.execute_script(js) #执行js代码
#
# input.send_keys('小米11')
#
#
# button=browser.find_element_by_xpath('//div[@class="form"]/button')
# button.click()