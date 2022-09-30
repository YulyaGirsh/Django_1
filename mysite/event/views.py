from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.views.generic import ListView, DetailView, CreateView
from .utils import *
from .forms import *
from .models import *

menu = [{'title': 'Главная', 'url_name': 'home'}, {'title': 'О сайте', 'url_name': 'about'}, {'title':
                                                                                                  'Регистрация',
                                                                                              'url_name': 'login'},
        {'title':
             'Добавление записи',
         'url_name':
             'add'}]


class EventsHome(DataMixin, ListView):
    model = Events
    template_name = 'event/index.html'
    context_object_name = 'post'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Главная страница')
        # context = dict(list(context.items()) + list(c_def.items()))
        # context['menu'] = menu
        # context['title'] = 'Главная страница'
        # context['area_selected'] = 0
        return dict(list(context.items()) + list(c_def.items()))

    def get_queryset(self):
        return Events.objects.filter(is_published=True)


# class AddPost(LoginRequiredMixin, DataMixin, CreateView):
#     form_class = AddPostForm
#     template_name = 'event/add_post.html'
#     context_object_name = 'post'
#
#     def get_context_data(self, *, object_list=None, **kwargs):
#         context = super().get_context_data(**kwargs)
#         c_def = self.get_user_context(title='Добавление записи')
#         # context['menu'] = menu
#         # context['title'] = 'Добавление записи'
#         return dict(list(context.items()) + list(c_def.items()))
@login_required
def add_post(request, ):
    if request.method == 'POST':
        form = AddPostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = AddPostForm()
    context = {'post': form, 'menu': menu, 'title': 'Добавление информации о новом фестивале'}
    return render(request, 'event/add_post.html', context=context)

class CategoryShow(DataMixin, ListView):
    model = Events
    template_name = 'event/index.html'
    context_object_name = 'post'
    allow_empty = False

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        # context['menu'] = menu
        # context['title'] = 'Локация - ' + str(context['post'][0].cat)
        # context['area_selected'] = context['post'][0].cat_id
        c_def = self.get_user_context(title='Локация - ' + str(context['post'][0].cat), area_selected=context[
            'post'][0].cat_id)
        return dict(list(context.items()) + list(c_def.items()))

    def get_queryset(self):
        return Events.objects.filter(cat__slug=self.kwargs['area_slug'], is_published=True)


class ShowPost(DataMixin, DetailView):
    model = Events
    template_name = 'event/post.html'
    slug_url_kwarg = 'post_slug'
    context_object_name = 'post'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title=context['post'])
        # context['title'] = context['post']
        # context['menu'] = menu
        return dict(list(context.items()) + list(c_def.items()))


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
