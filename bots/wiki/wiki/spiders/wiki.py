# -*- coding: utf-8 -*-

from scrapy import Request
from scrapy.spiders import Spider
from wiki.items import WikiTeam, WikiPlayer
from database.models import Team, Player
from urllib.parse import urljoin

import time
import datetime

import re


class WikiSpider(Spider):
    name = "wiki"

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3879.0 Safari/537.36 Edg/78.0.249.1',
    }

    def start_requests(self):
        url = 'https://nba.hupu.com/teams'
        yield Request(url, headers = self.headers)

    def parse(self, response):
        secondary_url = response.css('a.a_teamlink::attr(href)').extract()
        for next_url in secondary_url:
            nurl = urljoin(response.url, next_url)
            yield Request(nurl, callback = self.parse_secondary, headers = self.headers)

    def parse_secondary(self, response):
        team = WikiTeam()

        details = response.css('div.font p::text').extract()

        team['joined'] = details[0].split('：')[1]
        team['arena'] = details[1].split(' ')[0].split('：')[1]
        team['area'] = details[1].split(' ')[1].split('：')[1]

        team['full_name'] = response.css('span.title-text::text').extract()[0].split('（')[0]
        team['short_name'] = response.css('title::text').extract()[0].split('|')[0].strip()
        team['full_en_name'] = response.css('span.title-text::text').extract()[0].split('（')[1].split('）')[0]

        players = response.css('div.x_list span.c2 a::text').extract()

        yield team

        for player_ in players:
            player = WikiPlayer()
            #player['team'] = team['short_name']

            name = player_.strip()
            namelist = re.split('-| ', name)

            player['first_name'] = namelist[0]
            player['last_name'] = namelist[1] if len(namelist) >= 2 else ''

            player['full_name'] = name.replace('-', '·')
            player['team'] = Team.objects.get(short_name = team['short_name'])
            yield player

