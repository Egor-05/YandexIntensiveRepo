# Generated by Django 3.2.16 on 2022-11-10 18:55

import django.db.models.deletion
from django.db import migrations, models

import catalog.validators


class Migration(migrations.Migration):

    dependencies = [
        ("catalog", "0010_auto_20221110_2127"),
    ]

    operations = [
        migrations.AlterField(
            model_name="catalogitem",
            name="photo",
            field=models.OneToOneField(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="catalog.photo",
                verbose_name="Превью",
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
    ]
