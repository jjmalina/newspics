from django.shortcuts import render
from articlefeed.models import Article, Topic, Image

def index(request):
	articles = Article.objects.batch_select('topics','images').order_by('-pub_date')[:10]
	return render(request, 'base.html', {'articles': articles})
