from django import template
from news.models import Category, Tag, Author
from django.db.models import F, Count

register = template.Library()


@register.inclusion_tag('news/blocks/category_tpl.html')
def get_menu_categories():
    # categories = Category.objects.annotate(cat=Count('posts', filter=F('posts__id'))).filter(cat__gt=0)
    categories = Category.objects.all()
    return {'categories': categories}


@register.inclusion_tag('news/blocks/tags_tpl.html')
def get_menu_tags():
    # categories = Category.objects.annotate(cat=Count('posts', filter=F('posts__id'))).filter(cat__gt=0)
    tags = Tag.objects.all()
    return {'tags': tags}


@register.inclusion_tag('news/blocks/authors_tpl.html')
def get_menu_authors():
    # categories = Category.objects.annotate(cat=Count('posts', filter=F('posts__id'))).filter(cat__gt=0)
    authors = Author.objects.all()
    return {'authors': authors}