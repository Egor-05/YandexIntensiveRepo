from django import forms


class FeedbackForm(forms.Form):
    text = forms.CharField(label="Введите текст", help_text="Введите свой отзыв")
