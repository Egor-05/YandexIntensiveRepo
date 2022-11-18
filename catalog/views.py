from django.shortcuts import render, get_object_or_404
from .models import CatalogItem

# Create your views here.


def item_list(request):
    items = CatalogItem.objects.filter(is_published=True).order_by('name')
    context = {'title': 'Список товаров', 'items': items}
    return render(request, "catalog.html", context)


def item_details(request, num):
    item = get_object_or_404(CatalogItem, id=num, is_published=True)
    a = [item.name, item.category.name, item.text, ', '.join([j.name for j in item.tags.all()])]
    context = {'title': 'Список товаров', 'item': a}
    return render(request, "item_details.html", context)
