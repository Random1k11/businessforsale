# -*- coding: utf-8 -*-
import scrapy


class BusinessforsaleItem(scrapy.Item):

    title                = scrapy.Field()
    location             = scrapy.Field()
    price                = scrapy.Field()
    revenue              = scrapy.Field()
    cash_flow            = scrapy.Field()
    business_description = scrapy.Field()
    dictionary_details   = scrapy.Field()
    listing_id           = scrapy.Field()
    SOURCE               = scrapy.Field()
    section              = scrapy.Field()
    URL                  = scrapy.Field()
