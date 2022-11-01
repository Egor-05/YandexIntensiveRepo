from django.test import TestCase, Client
from django.core.exceptions import ValidationError
from .models import CatalogCategory, CatalogTag, CatalogItem


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


class ModelsTests(TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.category = CatalogCategory.objects.create(
            name="Тестовая категория",
            slug="test-category-slug",
            is_published=True
        )
        cls.item = CatalogItem.objects.create(
            name="Товар",
            text="превосходно",
            is_published=True,
            category=cls.category
        )

    def test_item_word_validator_positive(self):
        item_count = CatalogItem.objects.count()

        self.item = CatalogItem(
            name="Товар",
            text="превосходно",
            is_published=True,
            category=self.category
        )

        self.item.full_clean()
        self.item.save()

        self.assertNotEqual(item_count, CatalogItem.objects.count())

    def test_item_word_validator_negative(self):
        item_count = CatalogItem.objects.count()

        with self.assertRaises(ValidationError):
            self.item1 = CatalogItem(
                name="Товар",
                text="test",
                is_published=True,
                category=self.category
            )

            self.item1.full_clean()
            self.item1.save()

        self.assertEqual(item_count, CatalogItem.objects.count())

    def test_tag_slug_validator_positive(self):
        tag_count = CatalogTag.objects.count()

        self.tag = CatalogTag(
            name="Тэг", slug="test-tag-slug", is_published=True, item=self.item
        )

        self.tag.full_clean()
        self.tag.save()

        self.assertNotEqual(tag_count, CatalogTag.objects.count())

    def test_tag_slug_validator_negative(self):
        tag_count = CatalogTag.objects.count()

        with self.assertRaises(ValidationError):
            self.tag = CatalogTag(
                name="Тэг", slug="шпголирои", is_published=True, item=self.item
            )

            self.tag.full_clean()
            self.tag.save()

        self.assertEqual(tag_count, CatalogTag.objects.count())

    def test_category_slug_validator_positive(self):
        category_count = CatalogCategory.objects.count()

        self.category1 = CatalogCategory(
            name="Категория",
            slug="test-category1-slug",
            is_published=True,
            weight=100
        )

        self.category1.full_clean()
        self.category1.save()

        self.assertNotEqual(category_count, CatalogCategory.objects.count())

    def test_category_slug_validator_negative(self):
        category_count = CatalogCategory.objects.count()

        with self.assertRaises(ValidationError):
            self.category1 = CatalogCategory(
                name="Категория", slug="тгнпн", is_published=True, weight=100
            )

            self.category1.full_clean()
            self.category1.save()

        self.assertEqual(category_count, CatalogCategory.objects.count())

    def test_category_weight_validator_positive(self):
        category_count = CatalogCategory.objects.count()

        self.category1 = CatalogCategory(
            name="Категория",
            slug="test-category1-slug",
            is_published=True, weight=100
        )

        self.category1.full_clean()
        self.category1.save()

        self.assertNotEqual(category_count, CatalogCategory.objects.count())

    def test_category_weight_validator_negative(self):
        category_count = CatalogCategory.objects.count()

        with self.assertRaises(ValidationError):
            self.category1 = CatalogCategory(
                name="Категория",
                slug="test-category1-slug",
                is_published=True,
                weight=0,
            )

            self.category1.full_clean()
            self.category1.save()

        self.assertEqual(category_count, CatalogCategory.objects.count())
