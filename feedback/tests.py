from django.test import TestCase, Client
from django.urls import reverse

from .forms import FeedbackForm

# Create your tests here.


class FormTests(TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.form = FeedbackForm()

    def test_text_label(self):
        text_label = self.form.fields['text'].label
        self.assertEqual(text_label, "Введите текст")

    def test_text_help_text(self):
        help_text = self.form.fields['text'].help_text
        self.assertEqual(help_text, "Введите свой отзыв")

    def test_form_context_is_right(self):
        response = Client().get(reverse("feedback:feedback"))
        self.assertIn('form', response.context)

    def test_redirect_is_correct(self):
        form_data = {
            "text": "123456789"
        }

        response = Client().post(
            reverse("feedback:feedback"),
            data=form_data,
            follow=True
        )

        self.assertRedirects(response, reverse("feedback:feedback"))