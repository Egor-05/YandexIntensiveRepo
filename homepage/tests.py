from django.test import TestCase, Client
from django.urls import reverse


# Create your tests here.
class StaticURLTests(TestCase):
    def test_homepage_endpoint(self):
        response = Client().get("/")
        self.assertEqual(response.status_code, 200)


class TaskPagesTest(TestCase):
    def test_homepage_context_is_right(self):
        response = Client().get(reverse("homepage:home"))
        self.assertIn('dct', response.context)