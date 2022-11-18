from django.shortcuts import render, get_object_or_404
from .models import CatalogItem, CatalogCategory

# Create your views here.


def item_list(request):
    lst = []
    categories = CatalogCategory.objects.published()
    print(categories)
    for i in categories:
        items = CatalogItem.objects.published(i, False)
        if items:
            lst.append([i.name, items])
    context = {'title': 'Список товаров', 'dct': lst}
    return render(request, "catalog.html", context)


def item_details(request, num):
    item = get_object_or_404(CatalogItem, id=num, is_published=True)
    context = {'title': 'Список товаров', 'item': item}
    return render(request, "item_details.html", context)
