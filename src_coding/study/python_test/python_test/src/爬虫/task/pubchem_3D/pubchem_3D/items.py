# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class Pubchem3DItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    obj_cid=scrapy.Field()
    down_src=scrapy.Field()
    cas=scrapy.Field()
    # 用来记录爬取失败数据的索引
    index=scrapy.Field()
    # 用来记录下载失败的CAS号
    query=scrapy.Field()
    # 记录爬取失败数据的列表
    pending_cas_list=scrapy.Field()