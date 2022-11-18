from django.shortcuts import render
from catalog.models import CatalogItem


def home(request):
    items = CatalogItem.objects.filter(is_published=True, is_on_main=True).order_by('name')
    context = {'title': 'Главная', 'items': items}
    return render(request, "homepage.html", context)
