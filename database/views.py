from django.shortcuts import render
from database.models import news_entry
from django.http import Http404, HttpResponse, HttpResponseNotFound

# Create your views here.
def news(request, news_id):
	articles = news_entry.objects.filter(id = news_id)

	if len(articles) == 0:
		return HttpResponseNotFound("None")

	article = {}
	article['title'] = articles[0].title
	article['source'] = articles[0].source
	article['content'] = articles[0].content
	article['image_url'] = articles[0].image
	article['published_time'] = articles[0].published
	article['url'] = request.path

	return render(request, 'news.html', article)
