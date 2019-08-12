from django.urls import path
from django.urls import re_path
from app.views import file_list, file_content

urlpatterns = [
    # Определите схему урлов с привязкой к отображениям .views.file_list и .views.file_content
    path('', file_list, name='file_list'),
    re_path('\d{4}-\d{2}-\d{2}\/', file_list),
    path('<date>/', file_content, name='file_list'),
    path('file_content/<name>', file_content, name='file_content'),
    path('1/', file_content, name='file_content'),
]
