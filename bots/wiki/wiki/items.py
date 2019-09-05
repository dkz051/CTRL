# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy_djangoitem import DjangoItem
from database.models import Team, Player

class WikiTeam(DjangoItem):
    django_model = Team

class WikiPlayer(DjangoItem):
    django_model = Player
