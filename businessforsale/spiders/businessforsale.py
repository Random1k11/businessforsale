# -*- coding: utf-8 -*-
import scrapy
from businessforsale.items import BusinessforsaleItem
from scrapy.utils.project import get_project_settings
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import os




class BusinessforsaleSpider(scrapy.Spider):

    name = 'businessforsale'
    start_urls = ['https://www.businessforsale.com/']
    login_page = 'https://www.businessforsale.com/login.html'


    def start_requests(self):
        if get_project_settings().get('LOGIN_REQUIRED') == 1:
            yield scrapy.Request(url=self.login_page, callback=self.login)
        else:
            yield scrapy.Request(url=self.start_urls[0], callback=self.parse, dont_filter=True)


    def login(self, response):
        options = Options()
        options.add_argument('--headless')
        browser = webdriver.Chrome(executable_path=os.getcwd() + '/chromedriver', options=options)
        browser.get('https://www.businessforsale.com/login.html')
        browser.find_element_by_xpath('//input[@name="username"]').send_keys(get_project_settings().get('LOGIN'))
        browser.find_element_by_xpath('//input[@name="password"]').send_keys(get_project_settings().get('PASSWORD'))
        browser.find_element_by_xpath('//div[@class="formBlock"]/input[@value="Login"]').click()
        cookies = browser.get_cookies()
        browser.close()
        yield scrapy.Request(url=self.start_urls[0], cookies=cookies, callback=self.parse)


    def parse(self, response):
        sections = get_project_settings().get('SECTIONS_TO_COLLECT_INFORMATION')
        if len(sections) == 0:
            sections = [None, None]
        business_categories = [i for i in response.xpath('//ul[@class="topcountrieshome"]/li/a/@href').extract() if 'franchises' not in i]
        for url in business_categories[sections[0]:sections[1]]:
            yield scrapy.Request(url, callback=self.parse_category_page)


    def parse_category_page(self, response):
        section = response.xpath('//h1/text()').extract_first()
        for url in response.xpath('//div[@class="propertyContent row"]//a/@href').extract():
            yield scrapy.Request(url, callback=self.parse_item, meta={'section': section})


    def parse_item(self, response):

        r = response.xpath('//*[@id="topheader"]/div[1]/div').extract()
        print(r)

        title = response.xpath('//div[@class="row"]//h1/text()').extract_first().strip()
        location = response.xpath('//div[@class="row"]//h1/following-sibling::p/text()').extract_first().strip()
        price = response.xpath('//h2/text()').extract_first().strip()
        if len(price) == 0:
            price = 'BUSINESS SOLD'
        revenue = response.xpath('//h4[contains(., "Revenue")]/text()').extract_first().strip()
        cash_flow = response.xpath('//h4[contains(., "Cash Flow")]/text()').extract_first().strip()
        business_description = ''.join([i.replace('\n', '').replace('\t', '').replace('\r', '').strip() for i in response.xpath('//div[@class="col-lg-12"]/text()').extract()]).strip()
        keys_details = [i.replace(':', '').replace('\r', '').strip() for i in response.xpath('//div[@class="row"]/div[@class="col-lg-3"]/h4/text()').extract()]
        values_details = [i.replace('\n', '').replace('\t', '').replace('\r', '').strip() for i in response.xpath('//h3[@class="borderbottom"]/following-sibling::div/div[@class="col-lg-9"]/p/text()').extract()]
        dictionary_details = str(dict(zip(keys_details, values_details)))
        listing_id = response.xpath('//b[contains(., "Listing")]/parent::span/text()').extract_first().strip()
        URL = response.url
        item = BusinessforsaleItem()

        item['title']                = title
        item['location']             = location
        item['price']                = price
        item['revenue']              = revenue
        item['cash_flow']            = cash_flow
        item['business_description'] = business_description
        item['dictionary_details']   = dictionary_details
        item['listing_id']           = listing_id
        item['SOURCE']               = get_project_settings().get('SOURCE')
        item['section']              = response.meta.get('section')
        item['URL']                  = URL

        yield item
