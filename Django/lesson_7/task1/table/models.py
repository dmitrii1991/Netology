from django.db import models


class Field(models.Model):
    sort_number = models.CharField(max_length=50, verbose_name='Порядковый номер')
    name = models.CharField(max_length=50, verbose_name='Имя')
    width = models.CharField(max_length=50, verbose_name='Ширина')

    class Meta:
        verbose_name = 'Поле таблицы'
        verbose_name_plural = 'Поля таблицы'

    def __str__(self):
        return self.name


class CsvPath(models.Model):
    path = models.FilePathField(max_length=200, verbose_name='Путь к CSV')

    class Meta:
        verbose_name = 'Путь к CSV'
        verbose_name_plural = 'Путь к CSV'

    def get_path(self):
        return self.path

    def set_path(self, path):
        self.pk = 1
        self.path = path
        self.save()

    def __str__(self):
        return self.path.replace('\\', '/').split('/')[-1]