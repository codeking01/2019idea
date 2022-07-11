import scrapy


class IpSpider(scrapy.Spider):
    name = 'ip'
    allowed_domains = ['ip.chinaz.com/getip.aspx']
    start_urls = ['http://www.baidu.com']

    def parse(self, response):
        print('********************************hhhhhhhhhhhh')
        print(response.text)