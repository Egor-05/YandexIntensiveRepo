from django.shortcuts import render

from catalog.models import CatalogCategory, CatalogItem


def home(request):
    lst = []
    categories = CatalogCategory.objects.published()
    for i in categories:
        items = CatalogItem.objects.published(i, True)
        if items:
            lst.append([i.name, items])
    context = {"title": "Главная", "dct": lst}
    return render(request, "homepage.html", context)
