from django.shortcuts import render, get_object_or_404
from .models import Article

def article_list(request, category_slug=None):
    articles = Article.objects
    return render(request,
                  'articles/list.html',
                   {'articles': articles})