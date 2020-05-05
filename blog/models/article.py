from django.db import models


class Article(models.Model):
    STATUS_MAP = {
        'DRAFT': 0,
        'PUBLIC': 1,
    }

    title = models.CharField(max_length=100)
    body = models.TextField()
    status = models.SmallIntegerField(
        choices=[(v, k) for k, v in STATUS_MAP.items()],
        default=0,
    )
    tags = models.ManyToManyField('ArticleTag', blank=True)
    created_dt = models.DateTimeField(auto_now_add=True)
    updated_dt = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
