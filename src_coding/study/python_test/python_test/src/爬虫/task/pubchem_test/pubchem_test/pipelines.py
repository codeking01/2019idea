# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
k=0
list=[]
# from pubchem_test.spiders.pub import PubSpider

import urllib.request
class PubchemTestPipeline:
    def process_item(self, item, spider):
        try :
            url = item.get('down_src')
            filename = './pic/' + str(item.get('cas')) + '.sdf'
            urllib.request.urlretrieve(url=url, filename=filename)
        except:
            print('**第{0}条数据下载失败，正在记录CAS号......'.format(item.get('index')))
            list.append(item.get('cas'))
            print(list)
        # print(item.get('pending_cas'))
        return item