# -*- coding: utf-8 -*-

###### LOGIN ######
# if you specify "1" it will be logged in
LOGIN_REQUIRED = 0
LOGIN = 'your_login'
PASSWORD = 'password'
###################

SOURCE = 'B4SALE'

UPDATE_VALUES_IN_DATABASE = True

SECTIONS_TO_COLLECT_INFORMATION = [0, 1]

# for all sections = []
# Accountancy For Sale = [0, 1]
# Alternative Health For Sale = [1, 2]
# American Restaurants For Sale = [2, 3]
# Auto Repair, Service & Parts For Sale = [2, 3]
# Bars For Sale = [3, 4]
# Building Maintenance For Sale = [4, 5]
# Building Services For Sale = [5, 6]
# Cafe Bars For Sale = [6, 7]
# Carpet & Flooring For Sale = [7, 8]
# Coffee Shops For Sale = [8, 9]
# Commercial Cleaning For Sale = [9, 10]
# Convenience & Grocery Stores = [10, 11]
# Corporate Training For Sale = [11, 12]
# Education & School Related For Sale = [12, 13]
# Fast Food - Franchises For Sale = [13, 14]
# Gas & Petrol Stations For Sale = [14, 15]
# Hair & Beauty Salons For Sale = [15, 16]
# Health & Safety For Sale = [16, 17]


BOT_NAME = 'businessforsale'

SPIDER_MODULES = ['businessforsale.spiders']
NEWSPIDER_MODULE = 'businessforsale.spiders'

CONNECTION_STRING = "sqlite:///businessforsale.db"

ITEM_PIPELINES = {
    'businessforsale.pipelines.BusinessforsalePipeline': 300,
}

DOWNLOADER_MIDDLEWARES = {
    'scrapy.downloadermiddlewares.useragent.UserAgentMiddleware': None,
    'scrapy_fake_useragent.middleware.RandomUserAgentMiddleware': 400,
}

LOG_LEVEL = 'ERROR'

ROBOTSTXT_OBEY = True

COOKIES_ENABLED = True
COOKIES_DEBUG = True
