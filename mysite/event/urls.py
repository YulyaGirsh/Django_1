from django.contrib import admin
from django.urls import path, re_path
from .views import *

urlpatterns = [
    path('', index, name='home'),
    path('cats/<int:catid>/', category, ),
    re_path(r'^archive/(?P<year>[0-9]{4})/', archive, name='year'),
    path('about/', about, name='about')
]
