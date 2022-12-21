# Scrapy settings for hardware_store_parser project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'hardware_store_parser'

SPIDER_MODULES = ['hardware_store_parser.spiders']
NEWSPIDER_MODULE = 'hardware_store_parser.spiders'

LOG_ENABLED = True
LOG_LEVEL = "DEBUG"

IMAGES_STORE = 'photos'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
USER_AGENT = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
CONCURRENT_REQUESTS = 8

# Configure a delay for requests for the same website (default: 0)
# See https://docs.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
DOWNLOAD_DELAY = 1
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
COOKIES_ENABLED = True

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
# DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'disp_react_aa=2; ggr-widget-test=1; rnd-blabla=RU; disp_delivery_ab=B; disp_abc_categories=A; _ym_uid=1663362721247643777; _ym_d=1663362721; _gcl_au=1.1.1830018411.1663362721; iap.uid=eb98146e8ff94e46894938fe3ad9d0bd; _regionID=34; lastConfirmedRegionID=34; tmr_lvid=23c32653f7fb0dd0f7dade9828405d8e; tmr_lvidTS=1663362722448; aplaut_distinct_id=9PmK6zICuPwP; _gaexp=GAX1.2.nXqPoCboQeq6kIs8HbpCBg.19326.3!Xi1sqcpVSR-nNyL5UiNZnQ.19323.x994!nlBequwkToCH1Nvg6DHtIw.19342.0; uxs_uid=35d9f900-3604-11ed-aa2f-675f2aca1265; cookie_accepted=true; user-geolocation=0%2C0; sawOPH=true; dtCookie=v_4_srv_2_sn_CB977B39DAD521C67FA3AE03BD9A3496_perc_26623_ol_1_app-3Ab82b63450c1d92de_0; GACookieStorage=GA1.2.310423551.1663362722; _ym_isad=2; _reactCheckout=true; _gid=GA1.2.246721982.1663622308; x-api-option=cce-292; _ga=GA1.2.310423551.1663362722; tmr_reqNum=96; qrator_jsr=1663624430.900.j5OAQLM9iO05iQh3-bo33rlurjcgbat53c3ismvlladilb0o4-00; _ga_Z72HLV7H6T=GS1.1.1663624430.5.0.1663624430.0.0.0; qrator_jsid=1663624430.900.j5OAQLM9iO05iQh3-bfhss65f6h19377gn5sjd46tq8pf97fu; qrator_ssid=1663624432.452.MLOBstmt9SjzjBfF-q4kb00canmivguab4tek7bqnccju1vtv',
#   'Accept-Language': 'ru'
# }

# Enable or disable spider middlewares
# See https://docs.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'hardware_store_parser.middlewares.HardwareStoreParserSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#DOWNLOADER_MIDDLEWARES = {
#    'hardware_store_parser.middlewares.HardwareStoreParserDownloaderMiddleware': 543,
#}

# Enable or disable extensions
# See https://docs.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See https://docs.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
   'hardware_store_parser.pipelines.HardwareStoreParserPipeline': 400,
   'hardware_store_parser.pipelines.PhotosPipeline': 200
}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
