from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from businessforsale.spiders.businessforsale import BusinessforsaleSpider
 
 
process = CrawlerProcess(get_project_settings())
process.crawl(BusinessforsaleSpider)
process.start()
