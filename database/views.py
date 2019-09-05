from django.shortcuts import render
from database.models import news_entry, Team, Player
from django.http import Http404, HttpResponse, HttpResponseNotFound

# Create your views here.
def news(request, news_id):
	articles = news_entry.objects.filter(id = news_id)

	if len(articles) == 0:
		return HttpResponseNotFound("The article specified does not exist")

	article = {}
	article['page_title'] = articles[0].title + " | CTRL"
	article['title'] = articles[0].title
	article['source'] = articles[0].source
	article['content'] = articles[0].content
	article['image_url'] = articles[0].image
	article['published_time'] = articles[0].published
	article['url'] = request.path

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
