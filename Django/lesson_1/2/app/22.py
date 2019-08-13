import os
import time, datetime

context = {
        'files': [],
    }

dirname = os.path.dirname(__file__)
path, _ = os.path.split(dirname)
path_catalog = os.path.join(path, 'files/')
for folderName, subfolders, filenames in os.walk(path_catalog):
    for filename in filenames:
        file = {}
        secc = os.path.getmtime(folderName + '/' + filename)
        secm = os.path.getctime(folderName + '/' + filename)
        file['name'] = filename
        file['ctime'] = datetime.datetime.strptime(time.strftime("%d %m %Y %H %M %S", time.localtime(secc)), "%d %m %Y %H %M %S")
        file['mtime'] = datetime.datetime.strptime(time.strftime("%d %m %Y %H %M %S", time.localtime(secm)), "%d %m %Y %H %M %S")
        context['files'].append(file)
print(context)

# def file_content(name):
#     dirname = os.path.dirname(__file__)
#     path, _ = os.path.split(dirname)
#     path_catalog = os.path.join(path, 'files/')
#
#     if os.path.isfile(path_catalog + name):
#         with open(path_catalog + name) as file:
#             data = file.read()
#         files = {
#             name: {
#                 'file_content': data
#             }
#         }
#         context = {'name': name, 'file_content': files[name]['file_content']}
#     print(context)
#
#
#
# file_content({'name': 'server.01'})