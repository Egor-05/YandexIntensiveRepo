# Generated by Django 3.2.16 on 2022-11-01 09:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="abstractmodelforcatalog",
            name="is_published",
            field=models.BooleanField(default=True,
                                      verbose_name="Is_published"),
        ),
        migrations.AlterField(
            model_name="abstractmodelforcatalog",
            name="name",
            field=models.CharField(default="",
                                   max_length=150,
                                   verbose_name="Название"),
        ),
    ]