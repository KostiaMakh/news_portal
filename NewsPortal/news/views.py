from django.db.models import Prefetch
from django.shortcuts import render
from django.views.generic import *
from .models import *


class Main_page(ListView):
    model = News
    template_name = 'news/index.html'
    extra_context = {
        'authors': Author.objects.order_by("?")[:3]
    }

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Главная'
        return context


class Category_page(ListView):
    model = Category


class Tag_page(ListView):
    model = Tag


# class Author_page(ListView):
#     model = Author


class Author_detail(DetailView):
    model = Author
    context_object_name = 'author'
    template_name = 'news/author_detail.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['publications'] = News.objects.filter(author__slug=self.kwargs['slug'])
        return context
