from django.shortcuts import render
from catalog.models import CatalogItem


def home(request):
    items = []
    for i in CatalogItem.objects.filter(is_on_main=True):
        items.append([i.name, i.category.name, i.text[:10], ', '.join([j.name for j in i.tags.all()]), i.id])
    items.sort(key=lambda x: x[0])
    return render(request, "homepage.html", {'title': 'Главная', 'items': items})
