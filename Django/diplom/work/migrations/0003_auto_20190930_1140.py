# Generated by Django 2.2.4 on 2019-09-30 08:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('work', '0002_bd_description'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='bd',
            options={'ordering': ['-description'], 'verbose_name': 'Телефон', 'verbose_name_plural': 'Телефоны'},
        ),
        migrations.AddField(
            model_name='bd',
            name='images',
            field=models.ImageField(blank=True, null=True, upload_to='media/', verbose_name='Изображения'),
        ),
        migrations.AlterField(
            model_name='bd',
            name='description',
            field=models.TextField(blank=True, db_index=True, null=True, verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='bd',
            name='launch',
            field=models.DateField(blank=True, null=True, verbose_name='Дата начало производства'),
        ),
        migrations.AlterField(
            model_name='bd',
            name='manufacturer',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='производитель'),
        ),
        migrations.AlterField(
            model_name='bd',
            name='price',
            field=models.FloatField(blank=True, null=True, verbose_name='цена'),
        ),
        migrations.AlterField(
            model_name='bd',
            name='title',
            field=models.CharField(max_length=50, verbose_name='название телефона'),
        ),
    ]