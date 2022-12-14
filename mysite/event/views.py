from django.contrib.auth import logout, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.core.paginator import Paginator
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, FormView
from .utils import *
from .forms import *
from .models import *

menu = [{'title': 'Главная', 'url_name': 'home'}, {'title': 'О сайте', 'url_name': 'contact'},
        {'title':
             'Добавление записи',
         'url_name':
             'add'}]


class EventsHome(DataMixin, ListView):
    paginate_by = 3
    model = Events
    template_name = 'event/index.html'
    context_object_name = 'post'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Главная страница')
        return dict(list(context.items()) + list(c_def.items()))

    def get_queryset(self):
        return Events.objects.filter(is_published=True)


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
        return dict(list(context.items()) + list(c_def.items()))


class RegisterUser(DataMixin, CreateView):
    form_class = RegisterUserForm
    template_name = 'event/register.html'
    success_url = reverse_lazy('login')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Регистрация')
        return dict(list(context.items()) + list(c_def.items()))

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('home')


class LoginUser(DataMixin, LoginView):
    form_class = LoginUserForm
    template_name = 'event/login.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Авторизация')
        return dict(list(context.items()) + list(c_def.items()))

    def get_success_url(self):
        return reverse_lazy('home')


def logout_user(request):
    logout(request)
    return redirect('home')


class ContactFormView(DataMixin, FormView):
    form_class = ContactForm
    template_name = 'event/contact.html'
    success_url = reverse_lazy('home')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Обратная связь')
        return dict(list(context.items()) + list(c_def.items()))

    def form_valid(self, form):
        print(form.cleaned_data)
        return redirect('home')


def about(request):
    return render(request, 'event/about.html', {'title': 'Информация о сайте', 'menu': menu})


def archive(request, year):
    if int(year) > 2022:
        return redirect('home', permanent=True)
    return HttpResponse(f'<h1>Архив по годам</h1><p>{year}</p>')


def pageNotFound(request, exception):
    return HttpResponseNotFound('Страница не найдена')
