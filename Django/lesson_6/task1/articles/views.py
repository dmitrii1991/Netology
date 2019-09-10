from django.shortcuts import render
from .models import Article, Profile

def show_articles(request):
    articles = Article.objects.all()
    context = {
        'articles': articles,
    }
    return render(
        request,
        'articles.html',
        context
    )


def show_article(request, id):
    user = Profile.objects.filter(user=request.user)
    user_p = user[0].user_pay
    if not user_p:
        user_p = False

    article = Article.objects.filter(id=id)[0]
    context = {
        'article': article,
        'user_pay': user_p
    }


    return render(
        request,
        'article.html',
        context
    )


