from django.contrib import admin
from django.urls import path, re_path
from .views import *

urlpatterns = [
    path('', index, name='home'),
    path('cats/<int:catid>/', category ),
    re_path(r'^archive/(?P<year>[0-9]{4})/', archive, name='year'),
    path('contact/', contact, name='contact'),
    path('login', login, name='login'),
    path('about', about, name='about'),
    path('post/<int:post_id>/', post, name='post'),
    path('area/<int:area_id>/', category, name='area'),
]
