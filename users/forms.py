from django import forms
from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from django.contrib.auth.models import User

from .models import Profile


class RegistrationForm(UserCreationForm):
    email = forms.CharField(
        label="Адрес почты", max_length=100, help_text="Введите свою почту"
    )

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    def save(self, commit=True):
        user = super(RegistrationForm, self).save(commit=False)
        user.email = self.cleaned_data["email"]
        Profile.objects.create(user=user)

        if commit:
            user.save()
        return user


class ChangeForm(forms.Form):
    password = forms.CharField(
        label="Пароль", help_text="Введите новый пароль", widget=forms.PasswordInput
    )
    email = forms.CharField(label="Адрес почты", help_text="Введите свою почту")
    birthday = forms.DateField(
        label="Дата рождения", help_text="Введите свою дату рождения"
    )
