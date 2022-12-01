from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404, redirect, render
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated

from .forms import ChangeForm, RegistrationForm
from .models import Profile


def registration(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration successful.")
            return redirect("/")
    else:
        form = RegistrationForm()
    return render(request, "auth/signup.html", {"form": form})


def users_list(request):
    profiles = User.objects.all()

    context = {"title": "Список пользователей", "users": profiles}
    return render(request, "users.html", context)


def user_details(request, num):
    user = get_object_or_404(User, id=num)
    context = {"title": "подробно о пользователе", "user": user}
    return render(request, "user_details.html", context)


@permission_classes((IsAuthenticated,))
def profile(request):
    if request.method == "POST":
        form = ChangeForm(request.POST)
        if form.is_valid():
            current_user = request.user
            current_user.email = form.cleaned_data["email"]
            current_user.password = form.cleaned_data["password"]
            current_user.save()
            prof = Profile.objects.get(user=current_user)
            prof.save()
            return redirect("/")
    else:
        form = ChangeForm()
    return render(request, "auth/profile.html", {"form": form})
