from django.contrib import admin

from .models.article import Article
from .models.article_tag import ArticleTag

# Register your models here.
admin.site.register(Article)
admin.site.register(ArticleTag)
