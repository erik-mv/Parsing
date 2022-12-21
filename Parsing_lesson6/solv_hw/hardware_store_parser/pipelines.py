# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import scrapy
# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from scrapy.pipelines.images import ImagesPipeline
from pymongo import MongoClient
import hashlib
from scrapy.utils.python import to_bytes


class HardwareStoreParserPipeline:
    def __init__(self):
        client = MongoClient('127.0.0.1', 27017)
        self.mongo_base = client.db_hardware_store

    def process_item(self, item, spider):
        if item:
            item['price'] = int(item['price'].replace(' ', ''))
            item['product_characteristics'] = dict(zip(item['product_characteristics_keys'], item['product_characteristics_values']))
            del item['product_characteristics_keys'], item['product_characteristics_values']
            collection = self.mongo_base[spider.name]
            collection.insert_one(item)
        return item


class PhotosPipeline(ImagesPipeline):
    def get_media_requests(self, item, info):
        if item['images']:
            for img in item['images']:
                try:
                    yield scrapy.Request(img)
                except Exception as e:
                    print(e)

    def item_completed(self, results, item, info):
        item['images'] = [itm[1] for itm in results if itm[0]]
        return item

    def file_path(self, request, response=None, info=None, *, item=None):
        print()
        image_guid = hashlib.sha1(to_bytes(request.url)).hexdigest()
        return f"full/{item['good_name']}/{image_guid}.jpg"
