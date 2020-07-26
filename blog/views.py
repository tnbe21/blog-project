import json
from django.core import serializers
from django.http import JsonResponse, HttpResponse
from django.views import generic

from .models.article import Article


LMT = 3

class BaseView(generic.View):
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # URLパラメータをすべてレスポンスのコンテキスト内に詰める
        context.update(self.kwargs)
        # TODO 年月ごとの記事数のリストの生成
        # TODO タグとそれに紐づく記事数のリストの生成
        return context


class IndexView(BaseView, generic.ListView):
    template_name = 'blog/index.html'

    def get_queryset(self):
        page_num = self.kwargs.get('page_num', 1)
        start = LMT * (page_num - 1)
        return Article.objects.filter(status=Article.STATUS_MAP['PUBLIC']).order_by('-created_dt')[start:(start + LMT)]


def top(req):
    page_num = int(req.GET.get('page_num', 1))
    start = LMT * (page_num - 1)
    articles = Article.objects.filter(status=Article.STATUS_MAP['PUBLIC']).order_by('-created_dt')[start:(start + LMT)]
    return _create_json_response(list(map(lambda a: a.to_dict(), articles)))


class MonthListView(BaseView, generic.ListView):
    template_name = 'blog/month_list.html'

    def get_queryset(self):
        year = self.kwargs.get('year')
        month = self.kwargs.get('month')
        page_num = self.kwargs.get('page_num', 1)
        start = LMT * (page_num - 1)
        return Article.objects.filter(status=Article.STATUS_MAP['PUBLIC']).order_by('-created_dt')[start:(start + LMT)]


class TagListView(BaseView, generic.ListView):
    template_name = 'blog/tag_list.html'

    def get_queryset(self):
        tag = self.kwargs.get('tag')
        page_num = self.kwargs.get('page_num', 1)
        start = LMT * (page_num - 1)
        return Article.objects.filter(status=Article.STATUS_MAP['PUBLIC']).order_by('-created_dt')[start:(start + LMT)]


class SearchResultListView(BaseView, generic.ListView):
    template_name = 'blog/search_result_list.html'

    params = {}

    def __get_params(self):
        if not self.params:
            query_params = self.request.GET
            self.params = {
                'word': query_params.get('w'),
                'page_num': query_params.get('p', 1),
            }

        return self.params

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(self.__get_params())
        return context

    def get_queryset(self):
        word, page_num = self.__get_params().values()
        print("word: {}".format(word))
        print("page_num: {}".format(page_num))
        return Article.objects.filter(status=Article.STATUS_MAP['PUBLIC']).order_by('-created_dt')[:3]


class DetailView(BaseView, generic.DetailView):
    model = Article
    queryset = Article.objects.filter(status=Article.STATUS_MAP['PUBLIC'])

def _create_json_response(content):
    return JsonResponse(content, safe=False, json_dumps_params={'ensure_ascii': False})

