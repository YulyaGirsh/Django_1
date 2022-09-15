from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseNotFound, Http404
from .models import *

menu = ['О сайте', 'Добавить статью', 'Обратная связь', 'Войти']


def index(request):
    post = Events.objects.all()
    return render(request, 'event/index.html', {'title': 'Главная страница', 'menu': menu, 'post':post})


def category(request, catid):
    return HttpResponse(f'<h1>Страница категорий</h1><p>{catid}</p>')


def about(request):
    return render(request, 'event/about.html', {'title': 'Информация о сайте', 'menu': menu})


def archive(request, year):
    if int(year) > 2022:
        return redirect('home', permanent=True)
    return HttpResponse(f'<h1>Архив по годам</h1><p>{year}</p>')


def pageNotFound(request, exception):
    return HttpResponseNotFound('Страница не найдена')
