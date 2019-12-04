from django.contrib import admin
from .models import Article

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['id', 'headline', 'image', 'created', 'updated', 'description']
    list_filter = ['created', 'updated']
    list_editable = ['headline', 'image', 'description']