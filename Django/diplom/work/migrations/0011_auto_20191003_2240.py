# Generated by Django 2.2.4 on 2019-10-03 19:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('work', '0010_auto_20191003_1931'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='bought',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='cart',
            name='total_number',
            field=models.IntegerField(default=1, verbose_name='Количество товара'),
        ),
    ]
