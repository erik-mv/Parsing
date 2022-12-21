# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from itemloaders.processors import MapCompose, TakeFirst


class HardwareStoreParserItem(scrapy.Item):
    good_name = scrapy.Field(output_processor=TakeFirst())
    price = scrapy.Field(output_processor=TakeFirst())
    link = scrapy.Field(output_processor=TakeFirst())
    images = scrapy.Field()
    product_characteristics_keys = scrapy.Field(input_processor=MapCompose(lambda x: x.strip()))
    product_characteristics_values = scrapy.Field(input_processor=MapCompose(lambda x: x.strip()))
    product_characteristics = scrapy.Field()
    _id = scrapy.Field()
