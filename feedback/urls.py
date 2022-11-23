from django.urls import path
import feedback.views as views


urlpatterns = [path("feedback/", views.get_feedback, name="feedback")]
