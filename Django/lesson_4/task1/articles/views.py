from django.views.generic import ListView
from django.shortcuts import render

from articles.models import Article, ArticleTags


def articles_list(request):
    template = 'articles/news.html'

    # используйте этот параметр для упорядочивания результатов
    # https://docs.djangoproject.com/en/2.2/ref/models/querysets/#django.db.models.query.QuerySet.order_by

    object_list = Article.objects.all()
    context['data'] = object_list
    context['tags'] = {}
    for item in object_list:
        context['tags'][item.id] = {}
        tags = ArticleTags.objects.all().filter(article=item.id).order_by('-published_at')
        context['tags'][item.id] = tags

    return render(request, template, context)
