# Generated by Django 3.2.16 on 2022-11-01 09:20

import catalog.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("catalog", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="catalogcategory",
            options={"verbose_name": "Категория",
                     "verbose_name_plural": "Категории"},
        ),
        migrations.AlterModelOptions(
            name="catalogitem",
            options={"verbose_name": "Товар",
                     "verbose_name_plural": "Товары"},
        ),
        migrations.AlterModelOptions(
            name="catalogtag",
            options={"verbose_name": "Tag"},
        ),
        migrations.AddField(
            model_name="catalogitem",
            name="category",
            field=models.OneToOneField(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="catalog.catalogcategory",
            ),
        ),
        migrations.AlterField(
            model_name="catalogcategory",
            name="slug",
            field=models.CharField(
                default="",
                max_length=200,
                unique=True,
                validators=[catalog.validators.only_chars_validator],
                verbose_name="Tag",
            ),
        ),
        migrations.AlterField(
            model_name="catalogcategory",
            name="weight",
            field=models.IntegerField(
                default=100,
                validators=[catalog.validators.num_compare_validator],
                verbose_name="Вес",
            ),
        ),
        migrations.AlterField(
            model_name="catalogitem",
            name="text",
            field=models.TextField(
                default="",
                validators=[catalog.validators.in_value_validator],
                verbose_name="Текст",
            ),
        ),
        migrations.AlterField(
            model_name="catalogtag",
            name="item",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to="catalog.catalogitem",
                verbose_name="Товар",
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
                verbose_name="Tag",
            ),
        ),
    ]
