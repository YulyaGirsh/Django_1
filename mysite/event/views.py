from django.shortcuts import render, redirect, get_object_or_404
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


def category(request, area_slug):
    ident_area = Area.objects.get(slug=area_slug)
    post = Events.objects.filter(cat_id=ident_area.pk)
    context = {'title': 'Отображение по рубрикам',
               'menu': menu,
               'post': post,
               'area_selected': area_slug}
    return render(request, 'event/index.html', context=context)


def post(request, post_slug):
    our_post = Events.objects.filter(slug=post_slug)
    post = get_object_or_404(Events, slug=post_slug)
    our_area = Area.objects.filter(pk=post.cat_id)
    context = {'title': post.title,
               'menu': menu,
               'post': post,
               'area_selected': post.cat_id,
               'content': post.content,
               'area_slug': our_area
               }
    return render(request, 'event/post.html', context=context)


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
