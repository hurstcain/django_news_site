from django.urls import path

from news.views import *

urlpatterns = [
    path('', HomeNews.as_view(), name='home'),
    path('category/<int:category_id>/', NewsCategory.as_view(), name='category'),
    path('news/<int:news_id>/', ViewNews.as_view(), name='view_news'),
    path('news/add/', AddNews.as_view(), name='add_news'),
]
