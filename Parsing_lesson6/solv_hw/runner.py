from twisted.internet import reactor
from scrapy.crawler import CrawlerRunner
from scrapy.utils.project import get_project_settings
from scrapy.utils.log import configure_logging
import sys

from hardware_store_parser.spiders.castorama_ru import CastoramaRuSpider

if __name__ == '__main__':
    search = "котел"
    if len(sys.argv) != 1:
        search = ' '.join(sys.argv[1:])

    configure_logging()
    settings = get_project_settings()
    runner = CrawlerRunner(settings)
    runner.crawl(CastoramaRuSpider, search=search)
    d = runner.join()
    d.addBoth(lambda _: reactor.stop())
    reactor.run()
