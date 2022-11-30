from django import forms


class RegistrationForm(forms.Form):
    login = forms.CharField(label="Имя пользователя", max_length=100, help_text="Введите свой отзыв")
    password = forms.CharField(label="Имя пользователя", max_length=100, help_text="Введите свой отзыв")
    password = forms.CharField(label="Имя пользователя", max_length=100, help_text="Введите свой отзыв")