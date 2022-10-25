from django.urls import path
import catalog.views as views


urlpatterns = [
    path('catalog/', views.item_list),
    path('catalog/<int:num>/', views.item_details),
]
