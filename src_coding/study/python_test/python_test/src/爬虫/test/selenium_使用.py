from selenium import webdriver
import json

# 创建浏览器操作对象
path = 'chromedriver.exe'
browser = webdriver.Chrome(path)

# 访问网址
# url='https://www.baidu.com'
# url='https://pubchem.ncbi.nlm.nih.gov/#query=115754-21-7'
# browser.get(url)
# 元素定位
# 根据id 来找到元素
# button=browser.find_element_by_id('su')
# print(button)
# name=browser.find_elements_by_name('wd')
# print(name)
# 下面这个选择的是一个元素，并不能获取里面的value等属性值
# find_elements_by_xpath 这个返回的是一个列表，不加s的 返回的是一个的元素
# button=browser.find_elements_by_xpath('//input[@id="su"]')
# print(button)
# 根据标签的名字来获取对象
# button=browser.find_elements_by_tag_name('input')
# print(button)
# 根据bs4语法来获取元素
# button=browser.find_elements_by_css_selector('#su')
# print(button)
# 查找链接的元素
# content=browser.find_element_by_link_text('新闻')
# content = browser.find_elements_by_xpath('//a[@class=" capitalized"]')


# src=content.get_attribute('class')
# print(src)
# print(content[0].get_attribute('href'))
# print(content[0].text)
# for i in range(len(content)):
#     print(content)
# cid: 115754-20-6
cid = input("请输入要查询的cid号")
# https://pubchem.ncbi.nlm.nih.gov/sdq/sdqagent.cgi?infmt=json&outfmt=json&query={%22select%22:%22*%22,%22collection%22:%22compound%22,%22where%22:{%22ands%22:[{%22cid%22:%2243803992%22}]},%22order%22:[%22cid,asc%22],%22start%22:1,%22limit%22:10,%22width%22:1000000,%22listids%22:0}
url = 'https://pubchem.ncbi.nlm.nih.gov/sdq/sdqagent.cgi?infmt=json&outfmt=json&query={%22select%22:%22*%22,%22collection%22:%22compound%22,%22where%22:{%22ands%22:[{%22cid%22:%22' + str(
    cid) + '%22}]},%22order%22:[%22cid,asc%22],%22start%22:1,%22limit%22:10,%22width%22:1000000,%22listids%22:0}'
browser.get(url)
# 获取网页数据
content=browser.page_source.split('">')[1].split('<')[0]
# print(content)
with open('cid.json','w',encoding='utf-8') as fp:
        fp.write(str(content))
#   'https://pubchem.ncbi.nlm.nih.gov/compound/21180297'
obj=json.load(open('cid.json','r',encoding='utf-8'))
obj_cid=obj["SDQOutputSet"][0]["rows"][0]["cid"]
src_url='https://pubchem.ncbi.nlm.nih.gov/compound/'+str(obj_cid)
# print(src_url)
browser.get(src_url)


# 地址头 https://pubchem.ncbi.nlm.nih.gov   //a/img[1]/@src
# src=browser.find_elements_by_xpath('//a/img/@src')
# print(browser.page_source)

# /image/img3d.cgi?&cid=43810289&t=s
# 链接地址
#  /rest/pug/compound/CID/43810289/record/SDF/?record_type=3d&response_type=save&response_basename=Conformer3D_CID_43810289
# 'https://pubchem.ncbi.nlm.nih.gov'+ /rest/pug/compound/CID/403/record/SDF/?record_type=3d&response_type=save&response_basename=Conformer3D_CID_403
src='https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/CID/'+str(obj_cid)+'/record/SDF/?record_type=3d&response_type=save&response_basename=Conformer3D_CID_'+str(obj_cid)
browser.get(src)

# text=browser.page_source
# # dic=text.json()
# print(text)
