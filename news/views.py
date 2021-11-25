from django.shortcuts import render, get_object_or_404, redirect

from news.models import News, Category
from news.forms import NewsForm


def index(request):
    news = News.objects.order_by('-created_at')
    context = {
        'news': news,
        'title': 'Список новостей'
    }

    return render(request, template_name='news/index.html', context=context)


def get_news_by_category(request, category_id):
    category = Category.objects.get(id=category_id)
    news = News.objects.filter(category_id=category_id)
    context = {
        'category': category,
        'news': news
    }

    return render(request, template_name='news/category.html', context=context)


def get_news_content(request, news_id):
    news_to_view = get_object_or_404(News, pk=news_id)
    context = {
        'news': news_to_view
    }

    return render(request, template_name='news/view_news.html', context=context)


def add_news(request):
    if request.method == 'POST':
        form = NewsForm(request.POST, request.FILES)
        if form.is_valid():
            news = News.objects.create(**form.cleaned_data)

            return redirect(news)
    elif request.method == 'GET':
        form = NewsForm()
    context = {
        'form': form
    }

    return render(request, template_name='news/add_news.html', context=context)
