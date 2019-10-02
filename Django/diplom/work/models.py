from django.db import models
from django.contrib.auth.models import User  # доступ к пользователям
from django.core.validators import MinValueValidator, MaxValueValidator  # 1-5 звезд - Для валидации формы

class Bd(models.Model):
    title = models.CharField(max_length=50, verbose_name='название товара')
    manufacturer = models.CharField(max_length=50, null=True, blank=True,  verbose_name='производитель')
    price = models.FloatField(null=True, blank=True, verbose_name='цена')
    launch = models.DateField(null=True, blank=True, verbose_name='Дата начало производства')
    description = models.TextField(null=True, blank=True, db_index=True, verbose_name='Описание')
    images = models.ImageField(null=True, blank=True, upload_to='media/', verbose_name='Изображения')
    сategory = models.ForeignKey('Category', on_delete=models.CASCADE, blank=True, null=True,  verbose_name='Категория')  # каждый товар => на 1 из всех категорий

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Товары'
        verbose_name = 'Товар'
        ordering = ['-description']


class Review(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Автор отзыва') # каждый отзыв  => на 1 из всех авторов/пользователей
    text = models.TextField(verbose_name='Отзыв')
    score = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)], verbose_name='оценка отзыва') # проверка (“валидаторов”) выполняемых для этого поля
    bd = models.ForeignKey('Bd',  on_delete=models.CASCADE, verbose_name='Отзывы о товаре') #  каждый отзыв => на 1 из всех товаров
    def __str__(self):
        return f'{self.author}'

    class Meta:
        verbose_name_plural = 'Отзывы'
        verbose_name = 'Отзыв'


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Категории'
        verbose_name = 'КатегорииКатегория'
        ordering = ['name']


class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE ,verbose_name='Владелец корзины')  # каждая козина => на 1 из всех пользователей
    total_number = models.IntegerField(verbose_name='Количество категорий товара', default=1)
    item = models.ManyToManyField('Bd', blank=True, verbose_name='Корзина для товаров')  # каждая карзина => каждый товар

    def __str__(self):
        return f'Корзина {self.user}'

    class Meta:
        verbose_name_plural = 'Корзины'
        verbose_name = 'Корзина'