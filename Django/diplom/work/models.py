from django.db import models

class Bd(models.Model):
    title = models.CharField(max_length=50, verbose_name='название телефона')
    manufacturer = models.CharField(max_length=50, null=True, blank=True,  verbose_name='производитель')
    price = models.FloatField(null=True, blank=True, verbose_name='цена')
    launch = models.DateField(null=True, blank=True, verbose_name='Дата начало производства')
    description = models.TextField(null=True, blank=True, db_index=True, verbose_name='Описание')
    images = models.ImageField(null=True, blank=True, upload_to='media/', verbose_name='Изображения',)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Телефоны'
        verbose_name = 'Телефон'
        ordering = ['-description']
