from django.shortcuts import render, get_object_or_404
from .models import Article

def article_list(request, category_slug=None):
    articles = Article.objects.filter(available=True)
    return render(request,
                  'shop/articles/list.html',
                   'articles': articles})