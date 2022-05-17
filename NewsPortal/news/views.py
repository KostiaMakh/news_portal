from django.db.models import Prefetch, F
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
    model = News
    context_object_name = 'news'
    template_name = 'news/category_page.html'
    paginate_by = 2

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category_page'] = Category.objects.get(slug=self.kwargs['slug'])
        return context

    def get_queryset(self):
        return News.objects.filter(is_published=True, category__slug=self.kwargs['slug'])


class Tag_page(ListView):
    model = Tag


class Author_detail(DetailView):
    model = Author
    context_object_name = 'author'
    template_name = 'news/author_detail.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['publications'] = News.objects.filter(author__slug=self.kwargs['slug'])
        return context


class News_detail(DetailView):
    model = News
    context_object_name = 'news'
    template_name = 'news/news_detail.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['authors'] = Author.objects.filter(news__slug=self.kwargs['slug'])
        context['tags'] = Tag.objects.filter(news__slug=self.kwargs['slug'])
        self.object.views = F('views') + 1
        self.object.save()
        self.object.refresh_from_db()
        return context

    def get_queryset(self):
        return News.objects.filter(is_published=True)


class Timeline(ListView):
    model = News
    context_object_name = 'news'
    template_name = 'news/timeline.html'
    paginate_by = 2

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
