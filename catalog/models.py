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
        verbose_name="Тэг",
    )
    weight = models.IntegerField(
        default=100, validators=[num_compare_validator], verbose_name="Вес"
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"


class CatalogTag(AbstractModelForCatalog):
    slug = models.CharField(
        unique=True,
        default="",
        validators=[only_chars_validator],
        max_length=200,
        verbose_name="Тэг",
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Тэг"
        verbose_name_plural = "Тэги"


class CatalogItem(AbstractModelForCatalog):
    text = models.TextField(
        default="",
        validators=[in_value_validator('превосходно', 'роскошно')],
        verbose_name="Текст"
    )
    category = models.ForeignKey(
        CatalogCategory, on_delete=models.CASCADE, verbose_name="Категория"
    )
    tags = models.ManyToManyField(CatalogTag, verbose_name="Тэги")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Товар"
        verbose_name_plural = "Товары"
