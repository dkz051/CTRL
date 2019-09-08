from django.shortcuts import render
from django.shortcuts import render_to_response
from database.models import News, Team, Player, Relation, Word
from django.http import Http404, HttpResponse, HttpResponseNotFound
from math import *

import jieba
import jieba.analyse

import datetime

PAGINATION = 10
EXCERPT = 200

# Create your views here.
def news(request, news_id):
	articles = News.objects.filter(id = news_id)

	if len(articles) == 0:
		return HttpResponseNotFound("The article specified does not exist")

	article = {}
	article['page_title'] = articles[0].title + " | NBA 新闻聚合"
	article['title'] = articles[0].title
	article['source'] = articles[0].source
	article['image_url'] = articles[0].image
	article['published_time'] = articles[0].published
	article['url'] = request.path
	article['origin'] = articles[0].url

	content = articles[0].content_display
	keywords = []
	for team in Team.objects.all():
		keywords.append((team.full_name, '<span tf="{0}"></span>'.format(team.id), '<a href="/team/{0}/">{1}</a>'.format(team.id, team.full_name)))
		keywords.append((team.short_name, '<span ts="{0}"></span>'.format(team.id), '<a href="/team/{0}/">{1}</a>'.format(team.id, team.short_name)))
		keywords.append((team.full_en_name, '<span te="{0}"></span>'.format(team.id), '<a href="/team/{0}/">{1}</a>'.format(team.id, team.full_en_name)))
	for player in Player.objects.all():
		if len(player.full_name) > 0:
			keywords.append((player.full_name, '<span pu="{0}"></span>'.format(player.id), '<a href="/team/{0}/">{1}</a>'.format(player.team_id, player.full_name)))
		if len(player.first_name) > 0:
			keywords.append((player.first_name, '<span pi="{0}"></span>'.format(player.id), '<a href="/team/{0}/">{1}</a>'.format(player.team_id, player.first_name)))
		if len(player.last_name) > 0:
			keywords.append((player.last_name, '<span pl="{0}"></span>'.format(player.id), '<a href="/team/{0}/">{1}</a>'.format(player.team_id, player.last_name)))
	keywords = sorted(keywords, key = lambda tup: -len(tup[0]))
	print(keywords)

	for keyword, tempo, link in keywords:
		content = content.replace(keyword, tempo)
	for keyword, tempo, link in keywords:
		content = content.replace(tempo, link)
	article['content'] = content

	return render(request, 'news.html', article)

def team(request, team_id, page_id = 1):
	teams = Team.objects.filter(id = team_id)

	if len(teams) == 0:
		return HttpResponseNotFound("No such team")

	team = {}
	team['full_name'] = teams[0].full_name
	team['full_en_name'] = teams[0].full_en_name
	team['joined'] = teams[0].joined
	team['area'] = teams[0].area
	team['arena'] = teams[0].arena
	team['url'] = request.path
	team['players'] = Player.objects.filter(team = teams[0])

	newss = []

	related_news = Relation.objects.filter(team_id = team_id)

	pages = ceil(related_news.count() / PAGINATION)

	if page_id <= 0 or page_id > pages:
		return HttpResponseNotFound("The page requested does not exist.")

	for relation in related_news.order_by('-news__published')[(page_id - 1) * PAGINATION : page_id * PAGINATION]:
		news = {}
		news['id'] = relation.news_id
		news['title'] = relation.news.title
		news['published'] = relation.news.published
		news['excerpt'] = relation.news.content_raw[0 : EXCERPT] + ('...' if EXCERPT < len(relation.news.content_raw) else '')
		newss.append(news)
	team['news'] = newss

	team['page_title'] = ('' if page_id == 1 else '第 {0} 页 | '.format(page_id)) + teams[0].full_name + " | NBA 新闻聚合"
	team['page'] = page_id
	team['pages'] = pages
	team['page_interval_first'] = max(1, page_id - 5)
	team['page_interval_last'] = min(pages, page_id + 5)
	team['page_interval'] = range(max(1, page_id - 5), min(pages + 1, page_id + 6))

	team['pagination_prefix'] = '/team/{0}/'.format(team_id)

	return render(request, 'team.html', team)

def index(request, page_id = 1):
	start_time = datetime.datetime.now()

	teams = []
	for team in Team.objects.all():
		newt = {}
		newt['id'] = team.id
		newt['name'] = team.short_name
		newt['count'] = Relation.objects.filter(team_id = team.id).count()
		teams.append(newt)
	teams = sorted(teams, key = lambda t: -t['count'])

	data = {}
	data['trend'] = teams

	newss = []

	news_count_total = News.objects.count()
	data['news_count'] = news_count_total
	pages = ceil(news_count_total / PAGINATION)

	if page_id <= 0 or page_id > pages:
		return HttpResponseNotFound("The page requested does not exist.")

	for news in News.objects.all().order_by('-published')[(page_id - 1) * PAGINATION : page_id * PAGINATION]:
		new = {}
		new['id'] = news.id
		new['title'] = news.title
		new['published'] = news.published
		new['excerpt'] = news.content_raw[0 : EXCERPT] + ('...' if EXCERPT < len(news.content_raw) else '')
		newss.append(new)
	data['news'] = newss

	data['page_title'] = 'NBA 新闻聚合' if page_id == 1 else '第 {0} 页 | NBA 新闻聚合'.format(page_id)
	data['page'] = page_id
	data['pages'] = pages
	data['page_interval_first'] = max(1, page_id - 5)
	data['page_interval_last'] = min(pages, page_id + 5)
	data['page_interval'] = range(max(1, page_id - 5), min(pages + 1, page_id + 6))

	data['pagination_prefix'] = '/'

	end_time = datetime.datetime.now()

	data['loading_time'] = (end_time - start_time).microseconds / 1000000
	data['url'] = request.path

	return render(request, 'index.html', data)

def search(request, keyword, page_id = 1):
	start_time = datetime.datetime.now()

	keywords = jieba.analyse.extract_tags(keyword, withWeight = True) # Note: check if stop words appear in result
	word_seg = []

	news_list = {}
	news_count = News.objects.count()
	for word in keywords:
		word_seg.append(word[0])
		words = Word.objects.filter(word = word[0])
		if words.count() != 0:
			indices = words[0].indices.split('|')
			indices_count = len(indices)
			idf = log(news_count / (1 + indices_count))
			for index in indices:
				(news_id, count) = index.split(',')
				news_id = int(news_id)
				count = int(count)
				tf = count / News.objects.get(id = news_id).word_count
				if news_id not in news_list:
					news_list[news_id] = tf * idf * word[1]
				else:
					news_list[news_id] += tf * idf * word[1]
	news_list = sorted(news_list.items(), key = lambda entry: (-entry[1], entry[0]))

	end_time = datetime.datetime.now()

	data = {}
	data['search_count'] = len(news_list)
	data['search_time'] = (end_time - start_time).microseconds / 1000000

	data['search_word'] = keyword
	data['search_seg'] = word_seg

	newss = []
	pages = ceil(len(news_list) / PAGINATION)

	if pages == 0:
		pages = 1
		data['search_none'] = True
	else:
		data['search_none'] = False

	if page_id <= 0 or page_id > pages:
		return HttpResponseNotFound("The page requested does not exist.")

	for entry in news_list[(page_id - 1) * PAGINATION : page_id * PAGINATION]:
		new = {}
		news = News.objects.get(id = entry[0])
		new['id'] = news.id
		new['published'] = news.published

		excerpt = news.content_raw[0 : EXCERPT] + ('...' if EXCERPT < len(news.content_raw) else '')
		title = news.title

		for i in range(len(word_seg)):
			excerpt = excerpt.replace(word_seg[i], '<span id={0}'.format(i))
			title = title.replace(word_seg[i], '<span id={0}'.format(i))

		for i in range(len(word_seg)):
			excerpt = excerpt.replace('<span id={0}'.format(i), '<span class="key">{0}</span>'.format(word_seg[i]))
			title = title.replace('<span id={0}'.format(i), '<span class="key">{0}</span>'.format(word_seg[i]))

		new['excerpt'] = excerpt
		new['title'] = title

		newss.append(new)
	data['news'] = newss

	data['page_title'] = '搜索结果 | NBA 新闻聚合' if page_id == 1 else '第 {0} 页 | 搜索结果 | NBA 新闻聚合'.format(page_id)
	data['page'] = page_id
	data['pages'] = pages
	data['page_interval_first'] = max(1, page_id - 5)
	data['page_interval_last'] = min(pages, page_id + 5)
	data['page_interval'] = range(max(1, page_id - 5), min(pages + 1, page_id + 6))

	data['pagination_prefix'] = '/search/{0}/'.format(keyword)
	data['url'] = request.path
	return render(request, 'search.html', data)

def page_not_found(request, exception):
	# data['error_msg'] = exception
	return render_to_response('404.html')

def bot_admin(request):
	data = {}
	data['url'] = request.path
	data['page_title'] = '爬虫管理后台 | NBA 新闻聚合'
	return render(request, 'bot.html', data)

def about(request):
	data = {}
	data['url'] = request.path
	data['page_title'] = '关于「NBA 新闻聚合」'
	return render(request, 'about.html', data)
