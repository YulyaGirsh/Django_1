from django.db import models
from django.urls import reverse


class Events(models.Model):
    title = models.CharField(max_length=250, verbose_name='Название')
    content = models.TextField(blank=True, verbose_name='Содержание статьи')
    photo = models.ImageField(upload_to='photo/%Y/%m/d/', verbose_name='Фото')
    time_create = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')
    time_update = models.DateTimeField(auto_now=True, verbose_name='Время обновления')
    is_published = models.BooleanField(default=True, verbose_name='Опубликовано')
    cat = models.ForeignKey('Area', on_delete=models.PROTECT, null=True, verbose_name='Место проведения')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post', kwargs={'post_id': self.pk})
    class Meta:
        verbose_name = 'Фестиваль'
        verbose_name_plural = 'Фестивали'
        ordering = ['title']


class Area(models.Model):
    name = models.CharField(max_length=200, db_index=True, verbose_name='Локация')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('area', kwargs={'area_id': self.pk})
    class Meta:
        verbose_name = 'Локация'
        verbose_name_plural = 'Локации'
        ordering = ['id']
