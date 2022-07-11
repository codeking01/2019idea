import scrapy


class PubchemSpider(scrapy.Spider):
    name = 'Pubchem'
    allowed_domains = ['https://pubchem.ncbi.nlm.nih.gov']
    start_urls = ['https://pubchem.ncbi.nlm.nih.gov/#query=57-27-2']

    def parse(self, response):
        # pass
        print('********************************************')
        # 链接的整体对象  //main/div//a[@class=" capitalized"]
        # print(response) [@class="f-medium p-sm-top p-sm-bottom f-1125"]/a/@href
        src_list=response.xpath('//div/a')
        print(src_list)
        # for src in src_list:
        #     src=src.xpath('./@href')
        #     print(src)
        # yield src
