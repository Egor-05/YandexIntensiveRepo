from django import forms


class FeedbackForm(forms.Form):
    text = forms.CharField(label="Введите текст", max_length=100, help_text="Введите свой отзыв")