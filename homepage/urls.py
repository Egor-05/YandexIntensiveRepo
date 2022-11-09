from django.urls import path
import homepage.views as views


urlpatterns = [path("", views.home, name='home')]
