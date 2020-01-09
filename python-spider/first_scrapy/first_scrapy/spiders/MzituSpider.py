# -*- coding: utf-8 -*-
from scrapy import Spider, Request
from first_scrapy.items import ImageItem

class MziTuSpider(Spider):
    name = 'MziTuSpider'
    allowed_domains = ['www.mzitu.com']
    start_urls = ['https://www.mzitu.com/mm/']

    def start_requests(self):
        headers = {
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.117 Safari/537.36',
            'referer': 'https://www.mzitu.com/'
        }
        yield Request('https://www.mzitu.com/mm/', self.parse, headers = headers)

    def parse(self, response):
        imageList = response.css('.postlist ul li')
        for image in imageList:
            item = ImageItem()
            item['id'] = image.css('a::attr("href")').extract_first().split('/')[3]
            item['url'] = image.css('a::attr("href")').extract_first()
            item['title'] = image.css('a img::attr("alt")').extract_first()
            item['thumb'] = image.css('a img::attr("data-original")').extract_first()
            yield item