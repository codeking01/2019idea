import scrapy


class A58tcSpider(scrapy.Spider):
    name = '58tc'
    allowed_domains = ['https://tj.58.com/job']
    start_urls = ['http://https://tj.58.com/job/']

    def parse(self, response):
        pass
