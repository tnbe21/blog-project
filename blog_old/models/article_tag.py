from django.db import models


class ArticleTag(models.Model):
    def __str__(self):
        return self.name

    name = models.SlugField(max_length=30, db_index=True)
    created_dt = models.DateTimeField(auto_now_add=True)
    updated_dt = models.DateTimeField(auto_now=True)
