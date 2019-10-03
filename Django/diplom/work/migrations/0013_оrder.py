# Generated by Django 2.2.4 on 2019-10-03 21:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('work', '0012_auto_20191003_2355'),
    ]

    operations = [
        migrations.CreateModel(
            name='Оrder',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('invoice', models.CharField(max_length=10, unique=True, verbose_name='Номер накладной')),
                ('done', models.BooleanField(default=False, verbose_name='Выполнен заказ')),
                ('date', models.DateTimeField(verbose_name='Дата заказа')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Владелец заказа')),
                ('сat', models.ManyToManyField(to='work.CartItem', verbose_name='1 товар корзины')),
            ],
            options={
                'verbose_name': 'Заказ',
                'verbose_name_plural': 'Заказы',
            },
        ),
    ]
