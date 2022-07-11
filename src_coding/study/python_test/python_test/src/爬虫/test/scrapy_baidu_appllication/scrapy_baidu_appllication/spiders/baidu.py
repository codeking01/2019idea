import scrapy
from scrapy_baidu_appllication.items import ScrapyBaiduAppllicationItem

class BaiduSpider(scrapy.Spider):
    name = 'baidu'
    # 允许的作用域  一般写的是host
    allowed_domains = ['wwww.baidu.com']
    start_urls = ['http://wwww.baidu.com/']

    def parse(self, response):
        # 这个response  就是相当于以前写的获取到的服务器请求到的
        # pass
        # print('山东菏泽曹县')
        base_src=response.xpath('//div[@id="lg"]/img/@src')
        # 这个xpath解析出来只能是一个对象
        print('---------------------')
        # print(src.extract_first())
        src='https:'+str(base_src.extract_first())
        print(src)
        print('---------------------')
        # 把数据传输给pic对象
        pic=ScrapyBaiduAppllicationItem(src=src)
        # 这个pic对象会传输给pipelines中的item
        yield pic