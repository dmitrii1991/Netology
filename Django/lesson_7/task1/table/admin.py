from django.contrib import admin

from .models import Field, CsvPath


admin.site.register(Field)

admin.site.register(CsvPath)
