import scrapy
from scrapy_58tc.items import Scrapy58TcItem

class TcSpider(scrapy.Spider):
    name = 'tc'
    allowed_domains = ['https://tj.58.com/job']
    start_urls = ['https://tj.58.com/job/pn1']
    poge=1
    base_url='https://tj.58.com/job/pn'

    def parse(self, response):
        # pass
        print('*************************')
        # //div//li[@class="job_item clearfix"]//a/span[@class="address"]
        # 获取一个整体的li,然后再慢慢遍历
        li_list=response.xpath('//div//li[@class="job_item clearfix"]')
        for i in li_list:
            # 工作地点 222个 有8个没有写地点
            place=response.xpath('.//a/span[@class="address"]/text()').extract_first()
            # 职位名称 230个  去除了8个
            name=response.xpath('.//a/span[@class="name"]/text()').extract_first()
            # 价格  222个 有8个没有
            price=response.xpath('.//p[@class="job_salary"]/text()').extract_first()
            # 将内容传递给job对象
            job=Scrapy58TcItem(place=place,name=name,price=price)
            yield job
        # 一共70页，全部爬取下来
        if self.page<70 :
            self.page=self.page+1
            url=self.base_url+str(self.page)
            # 由于业务逻辑一样所以再次调用 parse即可
            yield scrapy.Request(url=url,callback=self.parse)







