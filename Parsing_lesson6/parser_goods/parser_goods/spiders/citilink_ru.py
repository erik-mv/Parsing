import scrapy
from scrapy.http import HtmlResponse
from parser_goods.items import ParserGoodsItem
from scrapy.loader import ItemLoader


class CitilinkRuSpider(scrapy.Spider):
    name = 'citilink_ru'
    allowed_domains = ['citilink.ru']
    
    def __init__(self, name=None, **kwargs):
        super().__init__(name, **kwargs)
        
        self.start_urls = [f"https://www.citilink.ru/search/?text=Тепловые+завесы"]
        #self.start_urls = [f"https://www.citilink.ru/search/?text={kwargs.get('query')}"]

    def parse(self, response:HtmlResponse):
        pages_links = response.xpath("//div[@class='SearchResults']//a[contains(@class, 'ProductCardVertical__name')]")
        for link in pages_links:
            yield response.follow(link, callback=self.parse_goods)

    def parse_goods(self, response:HtmlResponse):
        loader = ItemLoader(item=ParserGoodsItem(), response=response)
        
        loader.add_xpath('name', "//h1/text()")
        loader.add_value('url', response.url)
        loader.add_xpath('price', "//div[@class='ProductHeader__price-block']//span[contains(@class, 'price-default_current-price')]/text()")
        loader.add_xpath('photos', "//img[contains(@class, 'PreviewList__image ')]/@src")
        yield loader.load_item()

        
        '''
        goods_name = response.xpath("//h1/text()").get()
        goods_url = response.url
        goods_price = response.xpath("//div[@class='ProductHeader__price-block']//span[contains(@class, 'price-default_current-price')]/text()").get()
        goods_photos = response.xpath("//img[contains(@class, 'PreviewList__image ')]/@src").getall()

        yield ParserGoodsItem(
            name=goods_name,
            url=goods_url,
            price=goods_price,
            photos=goods_photos
        )
        '''
