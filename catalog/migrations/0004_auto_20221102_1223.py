# Generated by Django 3.2.16 on 2022-11-02 09:23

import catalog.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("catalog", "0003_alter_catalogitem_category"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="catalogtag",
            options={"verbose_name": "Тэг", "verbose_name_plural": "Тэги"},
        ),
        migrations.RemoveField(
            model_name="catalogtag",
            name="item",
        ),
        migrations.AddField(
            model_name="catalogitem",
            name="tags",
            field=models.ManyToManyField(to="catalog.CatalogTag", verbose_name="Тэг"),
        ),
        migrations.AlterField(
            model_name="catalogcategory",
            name="slug",
            field=models.CharField(
                default="",
                max_length=200,
                unique=True,
                validators=[catalog.validators.only_chars_validator],
                verbose_name="Тэг",
            ),
        ),
        migrations.AlterField(
            model_name="catalogtag",
            name="slug",
            field=models.CharField(
                default="",
                max_length=200,
                unique=True,
                validators=[catalog.validators.only_chars_validator],
                verbose_name="Тэг",
            ),
        ),
    ]