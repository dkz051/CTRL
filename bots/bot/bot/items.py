# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy_djangoitem import DjangoItem
from database.models import News, Relation

class BotItem(DjangoItem):
    django_model = News

class RelationItem(DjangoItem):
    django_model = Relation
