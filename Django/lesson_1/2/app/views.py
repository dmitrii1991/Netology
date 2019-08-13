import os
import time
import datetime
from django.shortcuts import render

def file_list(request, date=None):
    template_name = 'index.html'
    context = {'files': []}

    dirname = os.path.dirname(__file__)
    path, _ = os.path.split(dirname)
    path_catalog = os.path.join(path, 'files/')

    for folderName, subfolders, filenames in os.walk(path_catalog):
        for filename in filenames:
            file = {}
            secc = os.path.getmtime(folderName + '/' + filename)
            secm = os.path.getctime(folderName + '/' + filename)
            file['name'] = filename
            file['ctime'] = datetime.datetime.strptime(time.strftime("%d %m %Y", time.localtime(secc)),
                                                       "%d %m %Y")
            file['mtime'] = datetime.datetime.strptime(time.strftime("%d %m %Y", time.localtime(secm)),
                                                       "%d %m %Y")
            if date:
                y, m, d = date.split('-')
                date_file = datetime.datetime(year=int(y), month=int(m), day=int(d))
                if file['ctime'] == date_file:
                    context['files'].append(file)
            else:
                context['files'].append(file)
    return render(request, template_name, context)

def file_content(request, name):
    dirname = os.path.dirname(__file__)
    path, _ = os.path.split(dirname)
    path_catalog = os.path.join(path, 'files/')

    if os.path.isfile(path_catalog + name):
        with open(path_catalog + name) as file:
            data = file.read()
        files = {
            name: {
                'file_content': data
            }
        }
        context = {'name': name, 'file_content': files[name]['file_content']}

        return render(request, 'file_content.html', context)


