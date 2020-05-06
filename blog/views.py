from django.views import generic
from .models.article import Article


class IndexView(generic.ListView):
    template_name = 'blog/index.html'

    def get_queryset(self):
        return Article.objects.filter(status=Article.STATUS_MAP['PUBLIC']).order_by('-created_dt')[:3]


class DetailView(generic.DetailView):
    model = Article
    queryset = Article.objects.filter(status=Article.STATUS_MAP['PUBLIC'])
