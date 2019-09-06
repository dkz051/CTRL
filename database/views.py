from django.shortcuts import render
from database.models import News, Team, Player
from django.http import Http404, HttpResponse, HttpResponseNotFound
from math import *

PAGINATION = 10
EXCERPT = 200

# Create your views here.
def news(request, news_id):
	articles = News.objects.filter(id = news_id)

	if len(articles) == 0:
		return HttpResponseNotFound("The article specified does not exist")

	article = {}
	article['page_title'] = articles[0].title + " | CTRL"
	article['title'] = articles[0].title
	article['source'] = articles[0].source
	article['image_url'] = articles[0].image
	article['published_time'] = articles[0].published
	article['url'] = request.path
	# article['content'] = articles[0].content_display

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

def team(request, team_id):
	teams = Team.objects.filter(id = team_id)

	if len(teams) == 0:
		return HttpResponseNotFound("No such team")

	team = {}
	team['page_title'] = teams[0].full_name + " | CTRL"
	team['full_name'] = teams[0].full_name
	team['full_en_name'] = teams[0].full_en_name
	team['joined'] = teams[0].joined
	team['area'] = teams[0].area
	team['arena'] = teams[0].arena
	team['url'] = request.path
	team['players'] = Player.objects.filter(team = teams[0])

	return render(request, 'team.html', team)

def index(request, page_id = 1):
	page_id = int(page_id)

	teams = []
	for team in Team.objects.all():
		newt = {}
		newt['id'] = team.id
		newt['name'] = team.short_name
		newt['count'] = team.news_count
		teams.append(newt)
	teams = sorted(teams, key = lambda t: -t['count'])

	data = {}
	data['trend'] = teams

	newss = []
	pages = ceil(News.objects.count() / PAGINATION)
	for news in News.objects.all().order_by('-published')[(page_id - 1) * 10 : page_id * 10]:
		new = {}
		new['id'] = news.id
		new['title'] = news.title
		new['published'] = news.published
		new['excerpt'] = news.content_raw[0 : EXCERPT] + ('...' if EXCERPT < len(news.content_raw) else '')
		new['source'] = news.source
		newss.append(new)
	data['news'] = newss

	data['page'] = page_id
	data['pages'] = pages
	data['page_interval_first'] = max(1, page_id - 5)
	data['page_interval_last'] = min(pages, page_id + 5)
	data['page_interval'] = range(max(1, page_id - 5), min(pages + 1, page_id + 6))
	return render(request, 'index.html', data)
