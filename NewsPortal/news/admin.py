from django.contrib import admin
from django import forms
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django.utils.safestring import mark_safe
from .models import *


class PostAdminForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorUploadingWidget())
    content.label = "Пост"

    class Meta:
        model = News
        fields = '__all__'


class AuthorBiographyForm(forms.ModelForm):
    biography = forms.CharField(widget=CKEditorUploadingWidget())
    biography.label = "Биография"

    class Meta:
        model = Author
        fields = '__all__'


class CategoryForm(forms.ModelForm):
    description = forms.CharField(widget=CKEditorUploadingWidget())
    description.label = "Опписание категории"

    class Meta:
        model = Category
        fields = '__all__'


class NewsAdmin(admin.ModelAdmin):
    form = PostAdminForm
    save_on_top = True
    fields = ('title', 'author', 'category', 'content', 'photo', 'get_photo_to_card', 'tag', 'is_published', 'views', 'created_at',)
    readonly_fields = ('views', 'created_at', 'get_photo_to_card')
    list_filter = ('author', 'category', 'tag', 'is_published')
    search_fields = ('title', )
    list_display = ('pk', 'title', 'get_photo_to_list', 'category',  'is_published', 'views', 'created_at', 'slug',)
    list_editable = ('title', 'category',  'is_published')

    def get_photo_to_list(self, obj):
        if obj.photo:
            return mark_safe(f'<img src="{obj.photo.url}" alt="photo-{obj.title}" width="50px">')
        else:
            return '-'

    def get_photo_to_card(self, obj):
        if obj.photo:
            return mark_safe(f'<img src="{obj.photo.url}" alt="photo-{obj.title}" width="150px">')
        else:
            return '-'

    get_photo_to_list.short_description = 'Фото'
    get_photo_to_card.short_description = 'Фото'


class TagAdmin(admin.ModelAdmin):
    save_on_top = True
    fields = ('title', 'slug',)
    search_fields = ('title',)
    list_display = ('pk', 'title', 'slug',)
    list_editable = ('title',)


class AuthorAdmin(admin.ModelAdmin):
    save_on_top = True
    form = AuthorBiographyForm
    fields = ('name', 'surname', 'birthday', 'mail', 'biography', 'photo', 'get_photo_to_card')
    search_fields = ('name', 'surname',)
    readonly_fields = ('get_photo_to_card',)
    list_display = ('pk', 'slug', 'surname', 'name', 'get_photo_to_list')
    list_editable = ('surname', 'name',)

    def get_photo_to_list(self, obj):
        if obj.photo:
            return mark_safe(f'<img src="{obj.photo.url}" alt="photo-{obj.surname}-{obj.name}" width="50px">')
        else:
            return '-'

    def get_photo_to_card(self, obj):
        if obj.photo:
            return mark_safe(f'<img src="{obj.photo.url}" alt="photo-{obj.surname}-{obj.name}" width="150px">')
        else:
            return '-'

    get_photo_to_list.short_description = 'Фото'
    get_photo_to_card.short_description = 'Фото'


class CategoryAdmin(admin.ModelAdmin):
    form = CategoryForm
    save_on_top = True
    fields = ('title', 'description', 'photo', 'get_photo_to_card',)
    search_fields = ('title',)
    list_display = ('pk', 'title', 'slug', 'get_photo_to_list')
    readonly_fields = ('get_photo_to_card',)
    list_editable = ('title',)

    def get_photo_to_list(self, obj):
        if obj.photo:
            return mark_safe(f'<img src="{obj.photo.url}" alt="photo-{obj.title}" width="50px">')
        else:
            return '-'

    def get_photo_to_card(self, obj):
        if obj.photo:
            return mark_safe(f'<img src="{obj.photo.url}" alt="photo-{obj.title}" width="150px">')
        else:
            return '-'

    get_photo_to_list.short_description = 'Фото'
    get_photo_to_card.short_description = 'Фото'


admin.site.register(News, NewsAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Author, AuthorAdmin)

