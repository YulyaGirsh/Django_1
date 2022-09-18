from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseNotFound, Http404
from .models import *

menu = [{'title': 'О сайте', 'url_name': 'about'}, {'title': 'Регистрация', 'url_name': 'login'}, {'title':
                                                                                                       'Контакты',
                                                                                                   'url_name':
                                                                                                       'contact'}]


def index(request):
    post = Events.objects.all()
    context = {'title': 'Главная страница',
               'menu': menu, 'post': post,
               'area_selected': 0}

    return render(request, 'event/index.html', context)


def area(request, area_id):
    return HttpResponse(f'<h1>Страница категорий</h1><p>{area_id}</p>')


def category(request, area_id):
    post = Events.objects.filter(cat_id=area_id)
    context = {'title': 'Отображение по рубрикам',
               'menu': menu,
               'post': post,
               'area_selected': area_id}
    return render(request, 'event/index.html', context=context)


def post(request, post_id):
    return HttpResponse(f'Пост с идентификатором:{post_id}')


def contact(request):
    return render(request, 'event/about.html', {'title': 'Информация о сайте', 'menu': menu})


def about(request):
    return render(request, 'event/about.html', {'title': 'Информация о сайте', 'menu': menu})


def login(request):
    pass


def archive(request, year):
    if int(year) > 2022:
        return redirect('home', permanent=True)
    return HttpResponse(f'<h1>Архив по годам</h1><p>{year}</p>')


def pageNotFound(request, exception):
    return HttpResponseNotFound('Страница не найдена')
