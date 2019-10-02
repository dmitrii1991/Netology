from django.db import models
from django.contrib.auth.models import User  # доступ к пользователям
from django.core.validators import MinValueValidator, MaxValueValidator  # 1-5 звезд - Для валидации формы

class Bd(models.Model):
    title = models.CharField(max_length=50, verbose_name='название телефона')
    manufacturer = models.CharField(max_length=50, null=True, blank=True,  verbose_name='производитель')
    price = models.FloatField(null=True, blank=True, verbose_name='цена')
    launch = models.DateField(null=True, blank=True, verbose_name='Дата начало производства')
    description = models.TextField(null=True, blank=True, db_index=True, verbose_name='Описание')
    images = models.ImageField(null=True, blank=True, upload_to='media/', verbose_name='Изображения',)
    # reviews = models.ManyToManyField('Review', null=True, verbose_name='Отзывы о товаре') # Много товаров товар => Много отзывов
    сategory = models.ForeignKey('Category', on_delete=models.CASCADE, blank=True, null=True)  # Много товаров => 1 категория

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Телефоны'
        verbose_name = 'Телефон'
        ordering = ['-description']


class Review(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Автор отзыва') # 1 автор => Много отзывов
    text = models.TextField(verbose_name='Отзыв')
    score = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)], verbose_name='оценка отзыва') # проверка (“валидаторов”) выполняемых для этого поля
    bd = models.ForeignKey('Bd',  on_delete=models.CASCADE, verbose_name='Отзывы о товаре') # Много отзывов => 1 товар
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