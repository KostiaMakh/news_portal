from django import template
from news.models import Category, Tag, Author
from django.db.models import F, Count

register = template.Library()


@register.inclusion_tag('news/blocks/category_tpl.html')
def get_menu_categories():
    categories = Category.objects.annotate(cat=Count('news', filter=F('news__pk'))).filter(cat__gt=0)
    return {'categories': categories}


@register.inclusion_tag('news/blocks/tags_tpl.html')
def get_menu_tags():
    tags = Tag.objects.annotate(cat=Count('news', filter=F('news__pk'))).filter(cat__gt=0)
    return {'tags': tags}


@register.inclusion_tag('news/blocks/authors_tpl.html')
def get_menu_authors():
    authors = Author.objects.all()
    return {'authors': authors}