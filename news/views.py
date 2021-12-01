from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin

from news.models import News, Category
from news.forms import NewsForm


class HomeNews(ListView):
    queryset = News.objects.filter(is_published=True).select_related('category')
    template_name = 'news/index.html'
    context_object_name = 'news'
    paginate_by = 10


class NewsCategory(ListView):
    template_name = 'news/category.html'
    context_object_name = 'news'
    allow_empty = False
    paginate_by = 10

    def get_queryset(self):
        return News.objects.filter(is_published=True, category_id=self.kwargs['category_id']).select_related('category')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category'] = Category.objects.get(pk=self.kwargs['category_id'])

        return context


class ViewNews(DetailView):
    queryset = News.objects.filter(is_published=True).select_related('category')
    pk_url_kwarg = 'news_id'
    template_name = 'news/view_news.html'
    context_object_name = 'news'


class AddNews(LoginRequiredMixin, CreateView):
    form_class = NewsForm
    template_name = 'news/add_news.html'
    login_url = '/admin/'
