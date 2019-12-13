from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db import models
from django.db.models import Q
from django.db.models.signals import post_save


class Shop(models.Model):
    name = models.CharField(max_length=250)
    file_name = models.CharField(max_length=250)
    url_shop = models.URLField()


    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Поставщик'
        verbose_name_plural = 'Поставщики'


class Category(models.Model):
    shops = models.ManyToManyField(Shop)
    name = models.CharField(max_length=250)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Product(models.Model):
    name = models.CharField(max_length=250)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def get_info_product(self):
        return ProductInfo.objects.filter(product=self)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'


class ProductInfo(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE)
    name = models.CharField(max_length=250)
    quantity = models.IntegerField()
    price = models.FloatField()
    price_ = models.FloatField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Информация о товаре'
        verbose_name_plural = 'Информация о товарах'


class Parameter(models.Model):
    name = models.CharField(max_length=250)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Характеристика'
        verbose_name_plural = 'Характеристики'


class ProductParameter(models.Model):
    product_info = models.ForeignKey(ProductInfo, on_delete=models.CASCADE)
    parameter = models.ForeignKey(Parameter, on_delete=models.CASCADE)
    value = models.CharField(max_length=250)

    def __str__(self):
        return self.product_info

    class Meta:
        verbose_name = 'Характеристика товара'
        verbose_name_plural = 'Характеристики товаров'


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=250, choices=[
        ('1', 'one'),
        ('2', 'two'),
        ('3', 'three')
    ])

    def __str__(self):
        return f'order: {self.user.username} / {self.date} / {self.status}'

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE)
    quantity = models.IntegerField()

    def price(self):
        return ProductInfo.objects.filter(Q(product=self.product) | Q(shop=self.shop)).last().price

    def sum(self):
            return self.price * self.quantity

    class Meta:
        verbose_name = 'Товар в заказе'
        verbose_name_plural = 'Товары в заказе'


class Contact(models.Model):
    info = models.CharField(max_length=250)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    value = models.CharField(max_length=250)

    @classmethod
    def get_user_contacts(cls, user):
        return Contact.objects.filter(user=user)

    def __str__(self):
        return f'{self.user.username} / {self.info}'

    class Meta:
        verbose_name = 'Контакт'
        verbose_name_plural = 'Контакты'


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    email_as_username = models.EmailField(max_length=250, unique=True)
    company = models.CharField(max_length=250)
    patronymic = models.CharField(max_length=250)
    position = models.CharField(max_length=250)

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()