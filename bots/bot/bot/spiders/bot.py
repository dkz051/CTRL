# -*- coding: utf-8 -*-

from scrapy import Request
from scrapy.spiders import Spider
from bot.items import BotItem, RelationItem
from database.models import Team, Player, News, Relation
from urllib.parse import urljoin

import time, datetime, re
import logging

MAX_CRAWL = 40

class BotSpider(Spider):
    name = "bot"

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3879.0 Safari/537.36 Edg/78.0.249.1',
    }

    def start_requests(self):
        self.crawls_left = MAX_CRAWL
        url = 'https://voice.hupu.com/nba/1'
        yield Request(url, headers = self.headers)

    def parse(self, response):
        secondary_url = response.css('div.list-hd h4 a::attr(href)').extract()
        for next_url in secondary_url:
            if News.objects.filter(url = next_url).count() == 0:
                self.crawls_left -= 1
                yield Request(next_url, callback = self.parse_secondary, headers = self.headers)
                if self.crawls_left <= 0:
                    return
        next_pages = response.css('a.page-btn-prev::attr(href)').extract()
        if next_pages:
            yield Request(urljoin(response.url, next_pages[-1]), headers = self.headers)

    def parse_secondary(self, response):
        item = BotItem()
        item['title'] = response.css('h1.headline::text').extract()[0].strip()
        item['source'] = response.css('span.comeFrom a').extract()[0].strip()
        item['published'] = response.css('span#pubtime_baidu::text').extract()[0].strip()
        item['url'] = response.url
        images = response.css('div.artical-importantPic img::attr(src)').extract()
        if len(images) == 0:
            item['image'] = ''
        else:
            item['image'] = response.css('div.artical-importantPic img::attr(src)').extract()[0]

        content_raw = response.css('div.artical-main-content p::text').extract()
        content_display = '<p>' + '</p><p>'.join(content_raw) + '</p>'

        content_raw = ''.join(content_raw)

        item['content_raw'] = content_raw
        item['content_display'] = content_display
        yield item

        for teams in Team.objects.all():
            if content_raw.find(teams.short_name) != -1:
                relation = RelationItem()
                relation['team'] = teams
                relation['news'] = News.objects.get(url = item['url'])
                yield relation
                continue
            for player in Player.objects.filter(team_id = teams.id):
                if content_raw.find(player.last_name) != -1:
                    relation = RelationItem()
                    relation['team'] = teams
                    relation['news'] = News.objects.get(url = item['url'])
                    yield relation
                    break
