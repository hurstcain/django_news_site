from django import template

from news.models import Category, News

register = template.Library()


@register.simple_tag
def get_categories():
    return Category.objects.all()


@register.simple_tag
def define(value=None):
  return value


@register.filter
def timesince_filter(value):
    return value.split(',')[0]
