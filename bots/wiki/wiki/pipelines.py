# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

from wiki.items import WikiTeam, WikiPlayer

class WikiPipeline(object):
    def process_item(self, item, spider):
        if isinstance(item, WikiTeam):
            item.save()
        if isinstance(item, WikiPlayer):
            item.save()
        return item
