# -*- coding: utf-8 -*-
from scrapy import Request, Spider
from scrapy_selenium_demo.items import ProductItem


class JdSpider(Spider):
    name = 'jd'
    allowed_domains = ['www.jd.com']
    start_urls = ['http://www.jd.com/']

    def start_requests(self):
        base_url = 'https://search.jd.com/Search?keyword=iPhone&ev=exbrand_Apple'
        headers = {
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.117 Safari/537.36',
            'referer': 'https://www.jd.com/'
        }
        for page in range(1, self.settings.get('MAX_PAGE') + 1, 2):
            url = base_url + '&page=' + str(page)
            yield Request(url=url, callback=self.parse, meta={'page': page}, headers = headers)

    def parse(self, response):
        products = response.css('#J_goodsList .gl-item .gl-i-wrap')
        for product in products:
            item = ProductItem()
            item['image'] = product.css('.p-img a img::attr("src")').extract_first()
            item['price'] = product.css('.p-price i::text').extract_first()
            item['name'] = product.css('.p-name em::text').extract_first()
            item['commit'] = product.css('.p-commit a::text').extract_first()
            item['shop'] = product.css('.p-shop a::text').extract_first()
            item['icons'] = product.css('.p-icons .goods-icons::text').extract_first()
            yield item