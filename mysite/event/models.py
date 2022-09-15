from django.db import models

class Events(models.Model):
    title = models.CharField(max_length=250)
    photo = models.ImageField(upload_to='photo/%Y/%m/d/')
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=True)


    def __str__(self):
        return self.title
