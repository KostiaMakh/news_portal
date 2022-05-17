from django.db import models
from django.urls import reverse
from pytils.translit import slugify


class News(models.Model):
    slug = models.SlugField(max_length=150, verbose_name='url', unique=True)
    title = models.CharField(max_length=150, verbose_name='Тайтл')
    content = models.TextField(verbose_name='Текст поста')
    category = models.ForeignKey('category', on_delete=models.PROTECT, verbose_name='Категория')
    tag = models.ManyToManyField('tag', blank=True, verbose_name='Теги')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата публикации')
    photo = models.ImageField(upload_to='newsImg/media/%Y/%m/%d', blank=True, verbose_name='Загрузить фото')
    views = models.IntegerField(default=0, verbose_name='Просмотры')
    author = models.ManyToManyField('author', verbose_name='Автор')
    is_published = models.BooleanField(default=True, verbose_name='Опубликованно')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('news', kwargs={'slug': self.slug})

    def save(self, *args, **kwargs):
        self.slug = f'{slugify(self.pk)}-{slugify(self.title)}'
        super(News, self).save(*args, **kwargs)

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'
        ordering = ['-created_at']


class Tag(models.Model):
    slug = models.SlugField(max_length=150, verbose_name='url', unique=True)
    title = models.CharField(max_length=150, verbose_name='Тег')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('tag', kwargs={'slug': self.slug})

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Tag, self).save(*args, **kwargs)

    class Meta:
        verbose_name = 'Тег'
        verbose_name_plural = 'Теги'
        ordering = ['title']


class Category(models.Model):
    slug = models.SlugField(max_length=150, verbose_name='url', unique=True)
    title = models.CharField(max_length=150, verbose_name='Название категории')
    description = models.TextField(verbose_name='Описание категории', default='')
    photo = models.ImageField(upload_to='CategoryImg/media/%Y/%m/%d', blank=True, verbose_name='Загрузить фото')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('category', kwargs={'slug': self.slug})

    def save(self, *args, **kwargs):
        self.slug = f'{slugify(self.pk)}-{slugify(self.title)}'
        super(Category, self).save(*args, **kwargs)

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['title']


class Author(models.Model):
    slug = models.SlugField(max_length=255, verbose_name='url', unique=True, default='')
    name = models.CharField(max_length=150, verbose_name='Имя')
    surname = models.CharField(max_length=150, verbose_name='Фамилия')
    biography = models.TextField(verbose_name='Биография')
    birthday = models.DateField(verbose_name='Дата рождения')
    mail = models.EmailField(verbose_name='Адрес электронной почты')
    photo = models.ImageField(upload_to='AuthorsImg/media/%Y/%m/%d', blank=True, verbose_name='Загрузить фото')

    def __str__(self):
        return f'{self.surname} {self.name}'

    def get_absolute_url(self):
        return reverse('author', kwargs={'slug': self.slug})

    def save(self, *args, **kwargs):
        self.slug = f'{slugify(self.pk)}-{slugify(self.name)}-{slugify(self.surname)}'
        super(Author, self).save(*args, **kwargs)

    class Meta:
        verbose_name = 'Автор'
        verbose_name_plural = 'Авторы'
        ordering = ['surname']
