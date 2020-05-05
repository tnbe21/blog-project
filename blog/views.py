from django.shortcuts import render
from .models.article import Article


def index(request):
    article_list = Article.objects.filter(status=Article.STATUS_MAP['PUBLIC']).order_by('-created_dt')[:3]
    context = {
        'article_list': article_list,
    }
    return render(request, 'blog/index.html', context)

def detail(request, article_id):
    article = Article.objects.get(pk=article_id)
    context = {
        'article': article,
    }
    return render(request, 'blog/detail.html', context)
