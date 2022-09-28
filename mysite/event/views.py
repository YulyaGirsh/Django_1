from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.views.generic import ListView, DetailView, CreateView

from .forms import *
from .models import *

menu = [{'title': 'Главная', 'url_name': 'home'}, {'title': 'О сайте', 'url_name': 'about'}, {'title':
                                                                                                  'Регистрация',
                                                                                              'url_name': 'login'},
        {'title':
             'Добавление записи',
         'url_name':
             'add'}]


class EventsHome(ListView):
    model = Events
    template_name = 'event/index.html'
    context_object_name = 'post'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = menu
        context['title'] = 'Главная страница'
        context['area_selected'] = 0
        return context

    def get_queryset(self):
        return Events.objects.filter(is_published=True)


#     post = Events.objects.all()
#     context = {'title': 'Главная страница',
#                'menu': menu, 'post': post,
#                'area_selected': 0}
#
#     return render(request, 'event/index.html', context)

class AddPost(CreateView):
    form_class = AddPostForm
    template_name = 'event/add_post.html'
    context_object_name = 'form'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = menu
        context['title'] = 'Добавление записи'
        return context


# def add_post(request, ):
#     if request.method == 'POST':
#         form = AddPostForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             return redirect('home')
#     else:
#         form = AddPostForm()
#     context = {'post': form, 'menu': menu, 'title': 'Добавление информации о новом фестивале'}
#     return render(request, 'event/add_post.html', context=context)


class CategoryShow(ListView):
    model = Events
    template_name = 'event/index.html'
    context_object_name = 'post'
    allow_empty = False

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = menu
        context['title'] = 'Локация - ' + str(context['post'][0].cat)
        context['area_selected'] = context['post'][0].cat_id
        return context

    def get_queryset(self):
        return Events.objects.filter(cat__slug=self.kwargs['area_slug'], is_published=True)


# def category(request, area_slug):
#     ident_area = Area.objects.get(slug=area_slug)
#     post = Events.objects.filter(cat_id=ident_area.pk)
#     context = {'title': 'Отображение по рубрикам',
#                'menu': menu,
#                'post': post,
#                'area_selected': area_slug}
#     return render(request, 'event/index.html', context=context)

class ShowPost(DetailView):
    model = Events
    template_name = 'event/post.html'
    slug_url_kwarg = 'post_slug'
    context_object_name = 'post'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = context['post']
        context['menu'] = menu
        return context


# def post(request, post_slug):
#     our_post = Events.objects.filter(slug=post_slug)
#     post = get_object_or_404(Events, slug=post_slug)
#     our_area = Area.objects.filter(pk=post.cat_id)
#     context = {'title': post.title,
#                'menu': menu,
#                'post': post,
#                'area_selected': post.cat_id,
#                'content': post.content,
#                'area_slug': our_area
#                }
#     return render(request, 'event/post.html', context=context)


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
