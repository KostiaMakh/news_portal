from django import template


register = template.Library()


@register.inclusion_tag('news/blocks/pagination_tpl.html')
def get_pagination(page_obj):
    return {'page_obj': page_obj}