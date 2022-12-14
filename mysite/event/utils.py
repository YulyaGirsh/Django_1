from django.db.models import Count
from .models import *
from django.core.cache import cache
menu = [{'title': 'Главная', 'url_name': 'home'}, {'title': 'О сайте', 'url_name': 'contact'},
        {'title':
             'Добавление записи',
         'url_name':
             'add'}]


class DataMixin:
    # paginate_by = 5
    def get_user_context(self, **kwargs):
        cats = cache.get('cats')
        if not cats:
            cats = Area.objects.annotate(Count('events'))
            cache.set('cats', cats, 60)

        user_menu = menu.copy()
        if not self.request.user.is_authenticated:
            user_menu.pop(2)
        context = kwargs
        context['menu'] = user_menu
        context['title'] = 'Главная страница'
        context['cats'] = cats
        if 'area_selected' not in context:
            context['area_selected'] = 0
        return context
