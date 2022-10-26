from django.urls import path, re_path
import catalog.views as views


urlpatterns = [
    path("catalog/", views.item_list),
    re_path(r"catalog/(?P<num>[1-9]\d*)", views.item_details),
]
