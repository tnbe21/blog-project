from django.urls import path, register_converter

from . import views

class FourDigitYearConverter:
    regex = '[0-9]{4}'

    def to_python(self, value):
        return int(value)

    def to_url(self, value):
        return '%04d' % value


class MonthConverter:
    regex = '[0-9]{1,2}'

    def to_python(self, value):
        return int(value)

    def to_url(self, value):
        return value


class PageNumConverter:
    regex = '\d*'

    def to_python(self, value):
        return int(value) if value != '' else 1;

    def to_url(self, value):
        return value


register_converter(FourDigitYearConverter, 'yyyy')
register_converter(MonthConverter, 'mm')
register_converter(PageNumConverter, 'page')

app_name = 'blog'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('index/<int:page_num>', views.IndexView.as_view(), name='index'),
    path('month/<yyyy:year>/<mm:month>/<page:page_num>', views.MonthListView.as_view(), name='month_list'),
    path('tag/<slug:tag>/<page:page_num>', views.TagListView.as_view(), name='tag_list'),
    path('search', views.SearchResultListView.as_view(), name='search_result_list'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
]
