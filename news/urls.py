from django.urls import path

from news.views import index, get_news_by_category, get_news_content, add_news

urlpatterns = [
    path('', index, name='home'),
    path('category/<int:category_id>/', get_news_by_category, name='category'),
    path('news/<int:news_id>/', get_news_content, name='view_news'),
    path('news/add/', add_news, name='add_news'),
]
