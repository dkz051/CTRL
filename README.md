# NBA News Feed

___Long assignment 3 for THU Programming Practices course, September 2019___

## Description
A spider crawling [Hupu NBA News](https://voice.hupu.com/nba/1) and data for teams/players + a web system presenting the data crawled.

## Environment
* Python (3.7.3)
* Django (2.2.5)
* Scrapy (1.7.3)
* MySQL (5.7)
* Scrapyd (1.2.0)
* Jieba (0.39)
* pybloom-live (3.0.0)

See `requirements.txt` for dependency details.

## Running the Crawler

### Starting Scrapy Daemon
```bash
scrapyd
```

### Crawling Teams/Players
```bash
cd path/to/wiki/spider/including/setup/cfg
scrapyd-deploy ctrl -p wiki
curl http://localhost:6800/schedule.json -d project=wiki -d spider=wiki
```

### Deploying News Crawler
```bash
cd path/to/bot/spider/including/setup/cfg
scrapyd-deploy ctrl -p bot
```

## Starting Django Server
```bash
cd path/to/ctrl/with/manage/py
python3 manage.py runserver
```

The website will be running on `http://localhost:8000/`.

### Crawling News
Open `http://localhost:8000/bot/` and follow the instructions.
