# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
from scrapy.exporters import JsonLinesItemExporter
from datetime import datetime
#写出到json文件,使用内置的jsonlines 导出

class TiebaScrapyPipeline(object):
    def open_spider(self,spider):
        outfile=datetime.now().strftime("%Y-%m-%d")

        out = open( outfile+ ".json","wb")
        self.exporter = JsonLinesItemExporter(out,ensure_ascii=False)
        self.exporter.start_exporting()
    def close_spider(self,spider):
        self.exporter.finish_exporting()

    def process_item(self, item, spider):
        self.exporter.export_item(item)
        return item
