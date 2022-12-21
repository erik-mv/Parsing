# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from scrapy.pipelines.images import ImagesPipeline
from scrapy import Request


class ParserGoodsPipeline:
    def process_item(self, item, spider):
        return item


class CitilinkPhotosPipeline(ImagesPipeline):
    def get_media_requests(self, item, info):

        if item['photos']:
            for img in item['photos']:
                try:
                    yield Request(img)
                except Exception as e:
                    print(e)
    
    def item_completed(self, results, item, info):
        item['photos'] = [itm[1] for itm in results if itm[0]]
        return item
