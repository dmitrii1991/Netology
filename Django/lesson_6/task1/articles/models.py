from django.contrib.auth.models import User
from django.db import models


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, default="")
    user_pay = models.BooleanField(default=False, verbose_name='Оплатил контент?')

    def __str__(self):
        return str(self.user)


class Article(models.Model):
    headline = models.CharField(max_length=100, verbose_name='Заголовок', default="Статья")
    image = models.ImageField(upload_to='img/', height_field=None, width_field=None, max_length=100,
                              verbose_name='Тематическое изображение статьи', default="")
    content = models.TextField(verbose_name='Текст статья', default="")
    paid = models.BooleanField(default=False, verbose_name='Платную подписка')

    def __str__(self):
        return self.headline
