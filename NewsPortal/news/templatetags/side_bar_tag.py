from django import template
from news.models import Category, Tag, Author, News
from django.db.models import F, Count

register = template.Library()


@register.inclusion_tag('news/blocks/sidebar_tpl.html')
def get_sidebar():
    categories = Category.objects.annotate(cat=Count('news', filter=F('news__pk'))).filter(cat__gt=0)
    tags = Tag.objects.annotate(cat=Count('news', filter=F('news__pk'))).filter(cat__gt=0)
    # categories = Category.objects.all()
    # tags = Tag.objects.all()
    authors = Author.objects.all()
    return {'categories': categories,
            'tags': tags,
            'authors': authors}
