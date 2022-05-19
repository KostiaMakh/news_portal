from django.urls import path

from .views import *

urlpatterns = [
    path('', MainPage.as_view(), name='home'),
    path('category/<str:slug>/', CategoryPage.as_view(), name='category'),
    path('tag/<str:slug>/', TagPage.as_view(), name='tag'),
    path('author/<str:slug>/', AuthorDetail.as_view(), name='author'),
    path('news/<str:slug>/', NewsDetail.as_view(), name='news'),
    path('timeline/', Timeline.as_view(), name='timeline'),
    path('send/', sendMsg, name='sendMsg'),
    path('search/', Search.as_view(), name='search')
]
