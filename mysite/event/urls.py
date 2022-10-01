from django.contrib import admin
from django.urls import path, re_path
from .views import *

urlpatterns = [
    path('', EventsHome.as_view(), name='home'),
    path('cats/<int:catid>/', CategoryShow.as_view() ),
    re_path(r'^archive/(?P<year>[0-9]{4})/', archive, name='year'),
    path('contact/', contact, name='contact'),
    path('login', LoginUser.as_view(), name='login'),
    path('about', about, name='about'),
    path('post/<slug:post_slug>/', ShowPost.as_view(), name='post'),
    path('area/<slug:area_slug>/', CategoryShow.as_view(), name='area'),
    path('add/', add_post, name='add'),
    path('register/', RegisterUser.as_view(), name='register'),
    path('logout/', logout_user, name='logout'),
]
