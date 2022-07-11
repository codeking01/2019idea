import time
import json
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
# cid: 115754-20-6
cid_list=['115754-20-6']
for cid in cid_list:
    url = 'https://pubchem.ncbi.nlm.nih.gov/sdq/sdqagent.cgi?infmt=json&outfmt=json&query={%22select%22:%22*%22,%22collection%22:%22compound%22,%22where%22:{%22ands%22:[{%22cid%22:%22' + str(
        cid) + '%22}]},%22order%22:[%22cid,asc%22],%22start%22:1,%22limit%22:10,%22width%22:1000000,%22listids%22:0}'
    browser.get(url)
    print(browser.page_source)
    content=browser.page_source.split('">')[1].split('<')[0]
    # print(content)
    with open('cid_2.json','w',encoding='utf-8') as fp:
        fp.write(str(content))
    #   'https://pubchem.ncbi.nlm.nih.gov/compound/21180297'
    obj=json.load(open('cid_2.json','r',encoding='utf-8'))
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

    # 找到下载链接
    src='https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/CID/'+str(obj_cid)+'/record/SDF/?record_type=3d&response_type=save&response_basename=Conformer3D_CID_'+str(obj_cid)
    browser.get(src)
    time.sleep(1)