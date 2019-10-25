# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class TiebaScrapyItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # 主题id
    tid = scrapy.Field()
    #帖子标题
    title = scrapy.Field()
    #帖子时间 年月日
    createtime=scrapy.Field()
    #发帖人的昵称
    username = scrapy.Field()
    pass
