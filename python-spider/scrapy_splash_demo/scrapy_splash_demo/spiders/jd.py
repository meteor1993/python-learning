# -*- coding: utf-8 -*-
import scrapy
from scrapy_splash import SplashRequest


lua_script = """
function main(splash, args)
  splash:go(args.url)
    return {
      url = splash:url(),
      jpeg = splash:jpeg(),
      har = splash:har(),
      cookies = splash:get_cookies()
    }
end
"""


class JdSpider(scrapy.Spider):
    name = 'jd'
    allowed_domains = ['www.jd.com']
    start_urls = ['http://www.jd.com/']

    def start_requests(self):
        url = 'https://www.jd.com/'
        yield SplashRequest(url=url, callback=self.parse)

    def parse(self, response):
        self.logger.debug(response.text)
