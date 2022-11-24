from django.core.exceptions import ValidationError
from django.test import Client, TestCase
from django.urls import reverse

from .models import CatalogCategory, CatalogItem, CatalogTag


class StaticURLTests(TestCase):
    def test_catalog_page_endpoint(self):
        response = Client().get("/catalog/")
        self.assertEqual(response.status_code, 200)

    def negative_test_catalog_value_endpoint(self):
        for i in [2.24, -3, "2wjoiui2", 0]:
            url = f"/catalog/{i}/"
            response = Client().get(url)
            print(response.status_code)
            with self.subTest(url=url):
                self.assertEqual(response.status_code, 404)


class ModelsTests(TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.category = CatalogCategory.objects.create(
            name="Тестовая категория", slug="test-category-slug", is_published=True
        )
        cls.tag = CatalogTag.objects.create(
            name="Тэг",
            slug="test_tag_slug",
            is_published=True,
        )

    def test_item_word_validator_positive(self):
        item_count = CatalogItem.objects.count()

        self.item = CatalogItem(
            name="Товар", text="превосходно", is_published=True, category=self.category
        )
        self.item.full_clean()
        self.item.save()

        self.assertNotEqual(item_count, CatalogItem.objects.count())

    def test_item_word_validator_negative(self):
        item_count = CatalogItem.objects.count()

        with self.assertRaises(ValidationError):
            self.item1 = CatalogItem(
                name="Товар", text="test", is_published=True, category=self.category
            )

            self.item1.full_clean()
            self.item1.save()

        self.assertEqual(item_count, CatalogItem.objects.count())

    def test_tag_slug_validator_positive(self):
        tag_count = CatalogTag.objects.count()

        self.tag = CatalogTag(name="Тэг", slug="test-tag-slug", is_published=True)

        self.tag.full_clean()
        self.tag.save()

        self.assertNotEqual(tag_count, CatalogTag.objects.count())

    def test_tag_slug_validator_negative(self):
        tag_count = CatalogTag.objects.count()

        with self.assertRaises(ValidationError):
            self.tag = CatalogTag(name="Тэг", slug="шпголирои", is_published=True)

            self.tag.full_clean()
            self.tag.save()

        self.assertEqual(tag_count, CatalogTag.objects.count())

    def test_category_slug_validator_positive(self):
        category_count = CatalogCategory.objects.count()

        self.category1 = CatalogCategory(
            name="Категория", slug="test-category1-slug", is_published=True, weight=100
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
            name="Категория", slug="test-category1-slug", is_published=True, weight=100
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


class TaskPagesTest(TestCase):
    def test_catalog_context_is_right(self):
        response = Client().get(reverse("catalog:catalog"))
        self.assertIn("dct", response.context)
