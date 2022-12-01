from django.contrib.auth.views import *
from django.urls import path, re_path

from .views import profile, registration, user_details, users_list

urlpatterns = [
    path("login/", LoginView.as_view(template_name="auth/login.html")),
    path("logout/", LoginView.as_view(template_name="auth/logout.html")),
    path("registration/", registration),
    path(
        "password_change/", LoginView.as_view(template_name="auth/password_change.html")
    ),
    path(
        "password_change/done/",
        LoginView.as_view(template_name="auth/password_change_done.html"),
    ),
    path(
        "password_reset/", LoginView.as_view(template_name="auth/password_reset.html")
    ),
    path(
        "password_reset/done/",
        LoginView.as_view(template_name="auth/password_reset_done.html"),
    ),
    path(
        "reset/<uidb64>/<token>/",
        LoginView.as_view(template_name="auth/password_reset_confirm.html"),
    ),
    path(
        "reset/done/",
        LoginView.as_view(template_name="auth/password_reset_complete.html"),
    ),
    path("users/", users_list, name="users_list"),
    re_path(r"^users/(?P<num>[1-9]\d*)/$", user_details, name="user_details"),
    path("profile/", profile, name="change_password"),
]
