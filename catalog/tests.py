from django.test import TestCase, Client


# Create your tests here.
class StaticURLTests(TestCase):
    def test_catalog_page_endpoint(self):
        response = Client().get('/catalog/')
        self.assertEqual(response.status_code, 200)

    def test_catalog_info_page_endpoint(self):
        response = Client().get('/catalog/0/')
        self.assertEqual(response.status_code, 200)