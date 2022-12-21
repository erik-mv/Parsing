import scrapy
from scrapy.http import HtmlResponse
from hardware_store_parser.items import HardwareStoreParserItem
from scrapy.loader import ItemLoader


class CastoramaRuSpider(scrapy.Spider):
    name = 'castorama_ru'
    allowed_domains = ['castorama.ru']

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.start_urls = [f"https://www.castorama.ru/catalogsearch/result/?q={kwargs.get('search')}"]

    # start_urls = ['http://castorama.ru/']

    def parse(self, response: HtmlResponse):
        print(response.url)
        next_page = response.xpath("//a[@class='next i-next']/@href").get()
        if next_page:
            yield response.follow(next_page, callback=self.parse)
        links = response.xpath("//a[contains(@class, 'product-card__name')]")
        for link in links:
            yield response.follow(link, callback=self.goods_parse)

    def goods_parse(self, response: HtmlResponse):
        loader = ItemLoader(item=HardwareStoreParserItem(), response=response)
        loader.add_xpath('good_name', "//h1/text()")
        loader.add_xpath('price', "//span[@class='price']//text()")
        loader.add_value('link', response.url)
        loader.add_xpath('images', "//div[@class='js-zoom-container']//@data-src")
        loader.add_xpath('product_characteristics_keys', "//div[contains(@class, 'product-block')]//dl[contains(@class, 'specs-table')]/dt/span[contains(@class, 'specs-table__attribute-name')]/text()")
        loader.add_xpath('product_characteristics_values', "//div[contains(@class, 'specifications')]//dd[contains(@class, 'specs-table__attribute-value')]/text()")
        yield loader.load_item()
