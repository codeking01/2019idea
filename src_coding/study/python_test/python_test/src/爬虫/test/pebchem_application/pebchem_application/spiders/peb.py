import scrapy
import json
import requests
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
class PebSpider(scrapy.Spider):
    # 获取chrome handless 浏览器
    browser=share_browser()
    name = 'peb'
    allowed_domains = ['https://pubchem.ncbi.nlm.nih.gov']
    start_urls = ['http://https://pubchem.ncbi.nlm.nih.gov']

    def parse(self, response):
        # 需要定制的请求头
        headers = {
            'referer': 'https://pubchem.ncbi.nlm.nih.gov/'
        }
        cid_list = ['115754-20-6']

        for cid in cid_list:
            # 下面这个是为了获取需要链接的cid号
            url = 'https://pubchem.ncbi.nlm.nih.gov/sdq/sdqagent.cgi?infmt=json&outfmt=json&query={%22select%22:%22*%22,%22collection%22:%22compound%22,%22where%22:{%22ands%22:[{%22cid%22:%22' + str(
                cid) + '%22}]},%22order%22:[%22cid,asc%22],%22start%22:1,%22limit%22:10,%22width%22:1000000,%22listids%22:0}'
            response = requests.get(url=url, headers=headers)
            response.encoding = 'utf-8'
            # 下面这个json数据可以采集到
            json_content = response.text
            # print(page_content)
            with open('cid_4.json','w',encoding='utf-8') as fp:
                fp.write(str(json_content))
            #   'https://pubchem.ncbi.nlm.nih.gov/compound/21180297'
            obj=json.load(open('cid_4.json','r',encoding='utf-8'))
            obj_cid=obj["SDQOutputSet"][0]["rows"][0]["cid"]
            # print(obj_cid)

            # src_url='https://pubchem.ncbi.nlm.nih.gov/compound/'+str(obj_cid)
            # # 下载链接所在的页面
            # response=requests.get(url=src_url,headers=headers)

            down_src='https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/CID/'+str(obj_cid)+'/record/SDF/?record_type=3d&response_type=save&response_basename=Conformer3D_CID_'+str(obj_cid)
            browser.get(down_src)
            print('ok.....')
            time.sleep(2)
            # 关闭浏览器
            browser.quit()