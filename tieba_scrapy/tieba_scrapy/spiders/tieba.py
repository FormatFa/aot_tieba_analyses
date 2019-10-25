# -*- coding: utf-8 -*-
import scrapy
from scrapy.http.response.html import HtmlResponse
from tieba_scrapy.items import  TiebaScrapyItem
#贴吧主题爬取
class TiebaSpider(scrapy.Spider):
    name = 'tieba'
    allowed_domains = ['tieba.baidu.com']
    start_urls = [
        'https://tieba.baidu.com/f?kw=%E8%BF%9B%E5%87%BB%E7%9A%84%E5%B7%A8%E4%BA%BA&ie=utf-8&pn={}'.format(i*50)
        for i in range(0,230)
    ]

    def parse(self, response:HtmlResponse):
        #主题创建时间
        createtimes = response.xpath("//span[@title='创建时间']/text()").extract()
        #
        titles=[]
        tids=[]
        temp =response.xpath("//a[starts-with(@href,'/p/')]")
        for item in temp:
            titles.append(item.attrib["title"])
            tids.append(item.xpath('@href').extract_first() )

        usernames=response.xpath("//span[starts-with(@title,'主题作者')]/@title").extract()
        #50表示数据没错
        if len(usernames)==50 and len(titles)==50 and len(tids)==50 and len(createtimes)==50:
            for i in range(0,50):
                yield TiebaScrapyItem(tid=tids[i],
                title=titles[i],
                createtime=createtimes[i],
                username=usernames[i]
                )

