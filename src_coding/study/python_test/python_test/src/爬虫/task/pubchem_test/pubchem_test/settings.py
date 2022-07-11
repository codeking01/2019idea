# Scrapy settings for pubchem_test project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'pubchem_test'

SPIDER_MODULES = ['pubchem_test.spiders']
NEWSPIDER_MODULE = 'pubchem_test.spiders'

# 存放日志
LOG_FILE = 'log_pubchem_test.log'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'pubchem_test (+http://www.yourdomain.com)'

# Obey robots.txt rules
# ROBOTSTXT_OBEY = True

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://docs.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
# 打开请求延迟
DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
# 打开请求延迟
CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
#COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
DEFAULT_REQUEST_HEADERS = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language': 'en',
    'referer': 'https://pubchem.ncbi.nlm.nih.gov/',
}

# Enable or disable spider middlewares
# See https://docs.scrapy.org/en/latest/topics/spider-middleware.html
SPIDER_MIDDLEWARES = {
   'pubchem_test.middlewares.PubchemTestSpiderMiddleware': 543,
}



# PROXIES = [
#     # {'http':'118.24.219.151:16817'},
#     # {'http':'117.95.41.21:34854'},
#     # {'http':'49.89.143.39:3000'},
#     # {'http':'121.232.148.242:3256'},
#
#     '121.232.148.242:3256',
#     '121.230.210.58:3256',
#     '211.65.197.93:80',
#     '121.230.210.212:3256',
#     '182.84.144.119:3256',
#     '114.99.13.158:1133',
#     '117.88.246.101:3000',
#     '117.88.35.71:3000',
#     # '27.191.60.47:3256',
#     '121.230.211.227:3256',
#     '111.72.25.79:3256',
#     '47.75.132.50:8118',
#     '27.191.60.200:3256',
#     '47.100.14.22:9006',
#     '219.151.142.29:3128',
#     '211.65.197.93:80',
#     '117.94.222.240:3256',
# ]


# Enable or disable downloader middlewares
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
DOWNLOADER_MIDDLEWARES = {
   'pubchem_test.middlewares.PubchemTestDownloaderMiddleware': 543,
   # 'pubchem_test.middlewares.ProxyMiddleware': 544,

}

# Enable or disable extensions
# See https://docs.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}




# Configure item pipelines
# See https://docs.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
   'pubchem_test.pipelines.PubchemTestPipeline': 300,
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
