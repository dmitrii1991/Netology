from .models import Category

def category(request):
    # url_name = {
    #     'Смартфон': 'smartphones',
    #     'Одежда': 'clothes',
    # }
    # context = {}
    # for category in Category.objects.all():
    #     url = url_name.get(category.name)
    #     context["category_list"] = [category, url]
    return {'category_list': Category.objects.all()}