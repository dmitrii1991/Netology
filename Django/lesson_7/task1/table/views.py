import csv
import os

from django.shortcuts import render
from django.views import View
from django.conf import settings
from django.http import HttpResponse


class TableView(View):
    file_name = 'phones.csv'
    columns = [
        {'name': 'id', 'width': 1},
        {'name': 'name', 'width': 3},
        {'name': 'price', 'width': 2},
        {'name': 'release_date', 'width': 2},
        {'name': 'lte_exists', 'width': 1},
    ]

    def get(self, request):
        csv_file = os.path.join(settings.BASE_DIR, self.file_name)
        if csv_file:
            with open(csv_file, 'r') as f:
                header = []
                table = []
                table_reader = csv.reader(f, delimiter=';')
                for table_row in table_reader:
                    if not header:
                        header = {idx: value for idx, value in enumerate(table_row)}
                    else:
                        row = {header.get(idx) or 'col{:03d}'.format(idx): value
                               for idx, value in enumerate(table_row)}
                        table.append(row)

                result = render(request, 'table.html',
                                context={'columns': self.columns, 'table': table, 'csv_file': self.file_name})
            return result
        else:
            return HttpResponse('Указанный файл не найден', status=404)
