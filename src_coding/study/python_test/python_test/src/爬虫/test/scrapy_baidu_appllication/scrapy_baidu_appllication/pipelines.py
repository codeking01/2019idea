# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter

import urllib.request


class ScrapyBaiduAppllicationPipeline:

    def process_item(self, item, spider):
        # 把pic中的src传过来给下面要用到的url
        src = item.get('src')
        # 下载图片
        urllib.request.urlretrieve(url=src, filename='baidu.png')

        return item
