# Generated by Django 3.2.16 on 2022-11-10 18:17

import django.db.models.deletion
from django.db import migrations, models

import catalog.validators


class Migration(migrations.Migration):

    dependencies = [
        ("catalog", "0007_auto_20221108_2128"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="catalogitem",
            name="upload",
        ),
        migrations.RemoveField(
            model_name="photo",
            name="item",
        ),
        migrations.RemoveField(
            model_name="photo",
            name="photo",
        ),
        migrations.AddField(
            model_name="catalogitem",
            name="photo",
            field=models.OneToOneField(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="catalog.photo",
                verbose_name="Превью",
            ),
        ),
        migrations.AddField(
            model_name="photo",
            name="upload",
            field=models.ImageField(default="", upload_to="uploads/"),
            preserve_default=False,
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
        migrations.CreateModel(
            name="Photos",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("photo", models.ImageField(upload_to="photos/")),
                (
                    "item",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="photos",
                        to="catalog.catalogitem",
                    ),
                ),
            ],
        ),
    ]
