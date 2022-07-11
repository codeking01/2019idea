# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter

import urllib.request


class Pubchem3DPipeline:
    def process_item(self, item, spider):
        url = item.get('down_src')
        filename = './pic/Conformer3D_CID_' + str(item.get('cas')) + '.sdf'
        try :
            urllib.request.urlretrieve(url=url, filename=filename)
        except:
            print('**第{0}条数据下载失败，正在记录CAS号......'.format(item.get('index')))
            item['pending_cas_list'].append(item.get('cas'))
        print(item['pending_cas_list'])
        return item
