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


class CartItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Покупатель')  # каждый товар из козины имеет своего покупателя из всех пользователей
    total_number = models.IntegerField(verbose_name='Количество товара', default=1)
    item = models.ForeignKey('Bd', blank=True, on_delete=models.CASCADE, verbose_name='Корзина для товаров')  # каждый товар из козины ссылается на 1 товар из всех товаров
    bought = models.BooleanField(default=False, verbose_name='слелан ли заказ (якобы оплачено)')

    def __str__(self):
        return f'Товар из корзины {self.user} с {self.item} в количестве {self.total_number}'

    class Meta:
        verbose_name_plural = 'Корзины'
        verbose_name = 'Корзина'


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Владелец заказа')  # У каждого заказа может быть только 1 заказчик из списка пользователей
    cart = models.ManyToManyField(CartItem, verbose_name='1 товар корзины')  # У каждого заказа может быть много товаров из корзины (+ указано количество)
    invoice = models.CharField(max_length=10, unique=True, verbose_name='Номер накладной')
    done = models.BooleanField(default=False, verbose_name='Выполнен заказ')  # декоративный элемент
    date = models.DateTimeField(verbose_name='Дата заказа')
    total_number = models.FloatField(verbose_name='Общая сумма', default=0)

    def __str__(self):
        return f'Накладная №{self.invoice} '

    def display_item(self):
        return ', '.join([item.item.title  for item in self.cart.all()])
    display_item.short_description = 'заказанные товары'

    class Meta:
        verbose_name_plural = 'Заказы'
        verbose_name = 'Заказ'

