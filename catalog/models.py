from django.db import models
from django.utils.safestring import mark_safe
from PIL import Image
from sorl.thumbnail import get_thumbnail

from core.models import AbstractModelForCatalog

from .validators import (in_value_validator, num_compare_validator,
                         only_chars_validator)

# Create your models here.


class CategoryManager(models.Manager):
    def published(self):
        return self.get_queryset().filter(is_published=True).order_by("name")


class CatalogCategory(AbstractModelForCatalog):
    objects = CategoryManager()

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


class Photo(models.Model):
    name = models.CharField(max_length=150, default="", verbose_name="Название")
    upload = models.ImageField(upload_to="uploads/")

    @property
    def get_img(self):
        return get_thumbnail(self.upload, "300x300", crop="center", quality=51)

    def image_tmb(self):
        if self.upload:
            return mark_safe(f'<img src="{self.get_img.url}">')
        return "Нет изображения"

    image_tmb.short_description = "Превью"
    image_tmb.allow_tags = True

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Превью"
        verbose_name_plural = "Превью"


class ItemManager(models.Manager):
    def published(self, pk, is_on_main):
        if is_on_main:
            return (
                self.get_queryset()
                .filter(is_published=True, is_on_main=True, category=pk)
                .order_by("name")
            )
        else:
            return (
                self.get_queryset()
                .filter(is_published=True, category=pk)
                .order_by("name")
            )


class CatalogItem(AbstractModelForCatalog):
    objects = ItemManager()

    text = models.TextField(
        default="",
        validators=[in_value_validator("превосходно", "роскошно")],
        verbose_name="Текст",
    )
    category = models.ForeignKey(
        CatalogCategory, on_delete=models.CASCADE, verbose_name="Категория"
    )
    tags = models.ManyToManyField(CatalogTag, verbose_name="Тэги")
    photo = models.OneToOneField(
        Photo, on_delete=models.CASCADE, verbose_name="Превью", null=True, blank=True
    )
    is_on_main = models.BooleanField(default=False, verbose_name="Is_on_main")

    def image_tmb(self):
        if self.photo and self.photo.upload:
            return mark_safe(f'<img src="{self.photo.get_img.url}">')
        return "Нет изображения"

    image_tmb.short_description = "Превью"
    image_tmb.allow_tags = True

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Товар"
        verbose_name_plural = "Товары"


class Photos(models.Model):
    item = models.ForeignKey(
        CatalogItem, on_delete=models.CASCADE, related_name="photos"
    )
    photo = models.ImageField(upload_to="photos/")

    def save(self, *args, **kwargs):
        super(Photos, self).save(*args, **kwargs)
        img = Image.open(self.photo.path)
        if img.height > 300 or img.width > 300:
            img.thumbnail((300, 300))
        img.save(self.photo.path, quality=51, optimize=True)
