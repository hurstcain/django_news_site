from django import template
from django.db.models import Count, Q

from news.models import Category, News


register = template.Library()


@register.simple_tag
def get_categories():
    categories = Category.objects.annotate(news_count=Count('news', filter=Q(news__is_published=True))).filter(news_count__gt=0)
    return categories


@register.simple_tag
def define(value=None):
  return value


@register.filter
def timesince_filter(value):
    return value.split(',')[0]
