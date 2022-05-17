from django.urls import path

from .views import *

urlpatterns = [
    path('', Main_page.as_view(), name='home'),
    path('category/<str:slug>/', Category_page.as_view(), name='category'),
    path('tag/<str:slug>/', Tag_page.as_view(), name='tag'),
    path('author/<str:slug>/', Author_detail.as_view(), name='author'),
    path('news/<str:slug>/', News_detail.as_view(), name='news'),
    path('timeline/', Timeline.as_view(), name='timeline')
]
