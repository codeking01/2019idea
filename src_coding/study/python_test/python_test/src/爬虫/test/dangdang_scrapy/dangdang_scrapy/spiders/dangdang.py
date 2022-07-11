import scrapy
from dangdang_scrapy.items import DangdangScrapyItem

class DangdangSpider(scrapy.Spider):
    name = 'dangdang'
    allowed_domains = ['category.dangdang.com']
    start_urls = ['http://category.dangdang.com/cp01.49.05.01.00.00.html']
    # http://category.dangdang.com/pg2-cp01.49.05.01.00.00.html 第二页的地址
    page=1

    def parse(self, response):
        # pass
        print('**************************')
        # //ul[@class="bigimg"]/li
        li_list=response.xpath('//div[@id="search_nature_rg"]//ul[@class="bigimg"]/li')
        # print(li_list)
        # 获取标题，链接，价格
        for li in li_list:
            name=li.xpath('./a/@title').extract_first()
            #'http:' +  //product.dangdang.com/29295520.html
            src='http:'+li.xpath('./a/@href').extract_first()
            price=li.xpath('./p[@class="price"]/span[1]/text()').extract_first()
            # print(name,src,price)
            pic=response.xpath('.//img/@data-original').extract_first()
            if pic:
                pic=pic
            else:
                pic=response.xpath('.//img/@src').extract_first()
            book=DangdangScrapyItem(name=name,src=src,price=price,pic=pic)
            # 图片地址
            # print(pic)
            yield book
        if self.page<100:
            self.page+=1
            # http://category.dangdang.com/pg2-cp01.49.05.01.00.00.html
            url='http://category.dangdang.com/pg'+str(self.page)+'-cp01.49.05.01.00.00.html'
            yield scrapy.Request(url=url,callback=self.parse)