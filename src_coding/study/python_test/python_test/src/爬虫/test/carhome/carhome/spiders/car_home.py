import scrapy
from carhome.items import CarhomeItem

class CarHomeSpider(scrapy.Spider):
    name = 'car_home'
    allowed_domains = ['car.autohome.com.cn']
    start_urls = ['https://car.autohome.com.cn/price/brand-15-29.html']
    # https://car.autohome.com.cn/price/brand-15-0-0-2.html
    # https://car.autohome.com.cn/price/brand-15-0-0-i.html 第i页
    page=1
    base_url='https://car.autohome.com.cn/price'
    def parse(self, response):

        # pass
        print('************************************')
        # 所有内容的总汇 https://car.autohome.com.cn/price/brand-15.html
        # 名字和连接的对象 ：//div[@id="brandtab-1"]//a[@class="font-bold"] ,/text（）,/@href
        # 价格的对象 //div[@id="brandtab-1"]//span[@class="font-arial"]
        # 这个地方我犯错误了，这个我一开始写到是‘//div[@id="brandtab-1"]’，那么这样获取的则是整个大的div，则列表里面也就只有这一个了，仔细想想就懂了
        div_list=response.xpath('//div[@id="brandtab-1"]//div[@class="list-cont-main"]')
        # print(div_list.extract())
        for div in div_list:
            # extract() ‐‐‐》提取的是selector对象的是data
            # extract_first() ‐‐‐》提取的是selector列表中的第一个数据
            # 汽车系列
            name=div.xpath('.//a[@class="font-bold"]/text()').extract_first()
            # 汽车的链接
            src=div.xpath('.//a[@class="font-bold"]/@href').extract_first()
            # 汽车的价格
            price=div.xpath('.//span[@class="font-arial"]/text()').extract_first()
            print(name,src,price)
            car=CarhomeItem(name=name,src=src,price=price)
            yield car
        if self.page<3:
            self.page=self.page+1
            # 这个地方的地址别打错了，找BUG找了很久········
            url=self.base_url+'/brand-15-0-0-'+str(self.page)+'.html'
            # print(url)    #dont_filter = True
            yield scrapy.Request(url=url,callback=self.parse)

