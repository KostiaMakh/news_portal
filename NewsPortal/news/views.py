
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.mail import send_mail
from django.db.models import Prefetch, F
from django.shortcuts import render
from django.views.generic import *
from .models import *
from .forms import ContactAuthor
from NewsPortal.settings import EMAIL_HOST_USER


class Search(ListView):
    template_name = 'news/search.html'
    context_object_name = 'news'
    paginate_by = 3

    def get_queryset(self):
        return News.objects.filter(title__icontains=self.request.GET.get('search_field'))

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(Search, self).get_context_data(**kwargs)
        context['search_filed'] = f"s={self.request.GET.get('search_field')}&"
        context['search_val'] = self.request.GET.get('search_field')
        context['title'] = f"Search resul: '{self.request.GET.get('search_field')}'"
        return context


def sendMsg(request):
    author_mail = Author.objects.get(pk=request.POST['authorPk']).mail
    if request.method == 'POST':
        form = ContactAuthor(request.POST)
        if form.is_valid():
            fullMsg = f'''{form.cleaned_data['msg']}\n\nUser name: {form.cleaned_data['userName']};\nUser mail: {form.cleaned_data['userMail']}'''

            mail = send_mail(form.cleaned_data['subject'], fullMsg, EMAIL_HOST_USER,
                             [author_mail], fail_silently=False)
            if mail:
                messages.add_message(request, messages.SUCCESS, 'Письмо успешно отправленно')
            else:
                messages.add_message(request, messages.ERROR, 'Ошибка отправки')
        else:
            messages.add_message(request, messages.ERROR, 'Ошибка составления сообщения')
    else:
        form = ContactAuthor()
        messages.add_message(request, messages.ERROR, 'Ошибка отправки')
    context = {
        'form': form
    }
    return render(request, 'news/msg_s.html', context)


class MainPage(ListView):
    model = News
    template_name = 'news/index.html'
    extra_context = {
        'authors': Author.objects.order_by("?")[:3],
        'lastNews': News.objects.all(),
    }

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Главная'
        return context


class CategoryPage(ListView):
    model = News
    context_object_name = 'news'
    template_name = 'news/category_page.html'
    paginate_by = 2

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['newsPage'] = Category.objects.get(slug=self.kwargs['slug'])
        context['h1'] = f"Новости категории {str(Category.objects.get(slug=self.kwargs['slug'])).lower()}"
        return context

    def get_queryset(self):
        return News.objects.filter(is_published=True, category__slug=self.kwargs['slug'])


class TagPage(ListView):
    model = News
    context_object_name = 'news'
    template_name = 'news/tag_page.html'
    paginate_by = 2

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['newsPage'] = Tag.objects.get(slug=self.kwargs['slug'])
        context['h1'] = f"Новости с тегом #{str(Tag.objects.get(slug=self.kwargs['slug'])).lower()}"
        return context

    def get_queryset(self):
        return News.objects.filter(is_published=True, tag__slug=self.kwargs['slug'])


class AuthorDetail(DetailView):
    model = Author
    context_object_name = 'author'
    template_name = 'news/author_detail.html'
    extra_context = {
        'form': ContactAuthor
    }

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['publications'] = News.objects.filter(author__slug=self.kwargs['slug'])
        return context


class NewsDetail(DetailView):
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


