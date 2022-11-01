from django.db import models

# Create your models here.


class AbstractModelForCatalog(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=150,
                            default="",
                            verbose_name="Название")
    is_published = models.BooleanField(default=True,
                                       verbose_name="Is_published")
