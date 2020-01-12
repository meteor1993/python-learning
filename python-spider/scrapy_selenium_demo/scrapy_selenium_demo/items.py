# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ProductItem(scrapy.Item):
    collection = 'products'
    image = scrapy.Field()
    price = scrapy.Field()
    name = scrapy.Field()
    commit = scrapy.Field()
    shop = scrapy.Field()
    icons = scrapy.Field()