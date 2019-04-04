import sys

import Lib.scrapy.scrapy


class BrickSetSpider(Lib.scrapy.scrapy.):
    name = "brickset_spider"
    start_urls = ['http://brickset.com/sets/year-2016']