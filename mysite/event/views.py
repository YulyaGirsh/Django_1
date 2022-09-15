from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseNotFound, Http404


def index(request):
    return HttpResponse('Страница приложения мероприятий')


def category(request, catid):
    return HttpResponse(f'<h1>Страница категорий</h1><p>{catid}</p>')


def archive(request, year):
    if int(year) > 2022:
        return redirect('home', permanent=True)
    return HttpResponse(f'<h1>Архив по годам</h1><p>{year}</p>')


def pageNotFound(request, exception):
    return HttpResponseNotFound('Страница не найдена')
