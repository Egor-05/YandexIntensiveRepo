# from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def item_list(request):
    return HttpResponse('Список элементов', status=200)


def item_details(request, num):
    return HttpResponse('Подробно элемент', status=200)