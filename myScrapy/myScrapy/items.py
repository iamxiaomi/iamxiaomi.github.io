# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy import Item, Field


class MyscrapyItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()

    pass

class zolModelItem(scrapy.Item):
    catName=scrapy.Field()
    catLink=scrapy.Field()
    modelName=scrapy.Field()
    modelDes=scrapy.Field()

class zolCatItem(scrapy.Item):
    catName=scrapy.Field()
    catLink=scrapy.Field()


