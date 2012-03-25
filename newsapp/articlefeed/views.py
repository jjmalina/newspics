from django.shortcuts import render
from endless_pagination.decorators import page_template
from articlefeed.models import Article, Topic, Image


@page_template('article_feed.html')
def index(request, template='base.html', extra_context=None):
    articles = Article.objects.batch_select('topics','images').order_by('-pub_date')
    context = {}
    context['articles'] = articles
    if extra_context is not None:
        context.update(extra_context)
    return render(request, template, context)
