from django.shortcuts import render, get_object_or_404
from .models import CatalogItem

# Create your views here.


def item_list(request):
    items = []
    for i in CatalogItem.objects.filter(is_on_main=True):
        items.append([i.name, i.category.name, i.text[:10], ', '.join([j.name for j in i.tags.all()]), i.id])
    items.sort(key=lambda x: x[0])
    return render(request, "catalog.html", {'title': 'Список товаров', 'items': items})


def item_details(request, num):
    item = get_object_or_404(CatalogItem, id=num)
    return render(request, "item_details.html", {'title': 'Подробно о товаре',
                                                 'item': [item.name,
                                                          item.category.name,
                                                          item.text,
                                                          ', '.join(
                                                          [j.name for j in item.tags.all()]
                                                          )]})
