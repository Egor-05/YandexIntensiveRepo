from django.test import TestCase, Client


# Create your tests here.
class StaticURLTests(TestCase):
    def test_catalog_page_endpoint(self):
        response = Client().get("/catalog/")
        self.assertEqual(response.status_code, 200)

    def test_catalog_info_page_endpoint(self):
        response = Client().get("/catalog/1/")
        self.assertEqual(response.status_code, 200)

    def negative_test_catalog_value_endpoint(self):
        for i in [2.24, -3, "2wjoiui2", 0]:
            url = f"/catalog/{i}/"
            response = Client().get(url)
            with self.subTest(url=url):
                self.assertEqual(response.status_code, 404)

    def test_catalog_value_endpoint(self):
        for i in [1, 2, 200000000]:
            url = f"/catalog/{i}/"
            response = Client().get(url)
            with self.subTest(url=url):
                self.assertEqual(response.status_code, 200)
