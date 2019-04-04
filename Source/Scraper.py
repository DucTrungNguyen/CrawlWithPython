import sys

import Lib.scrapy.scrapy


class BrickSetSpider(Lib.scrapy.scrapy.spiders):
    name = "brickset_spider"
    start_urls = ['http://brickset.com/sets/year-2016']