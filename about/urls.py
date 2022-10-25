from django.urls import path
import about.views as views


urlpatterns = [
    path("about/", views.description)
]
