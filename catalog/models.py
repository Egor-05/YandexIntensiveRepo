from django.db import models
from .validators import in_value_validator, only_chars_validator, num_compare_validator
from core.models import AbstractModelForCatalog

# Create your models here.


class CatalogCategory(AbstractModelForCatalog):
    slug = models.CharField(
        unique=True,
        default="",
        validators=[only_chars_validator],
        max_length=200,
        verbose_name="Tag",
    )
    weight = models.IntegerField(
        default=100, validators=[num_compare_validator], verbose_name="Вес"
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"


class CatalogItem(AbstractModelForCatalog):
    text = models.TextField(
        default="", validators=[in_value_validator], verbose_name="Текст"
    )
    category = models.ForeignKey(
        CatalogCategory, on_delete=models.CASCADE, verbose_name="Категория"
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Товар"
        verbose_name_plural = "Товары"


class CatalogTag(AbstractModelForCatalog):
    slug = models.CharField(
        unique=True,
        default="",
        validators=[only_chars_validator],
        max_length=200,
        verbose_name="Tag",
    )
    item = models.ForeignKey(
        CatalogItem, on_delete=models.CASCADE, verbose_name="Товар"
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Tag"
