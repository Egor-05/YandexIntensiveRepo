from django.db import models


class Feedback(models.Model):
    text = models.TextField(verbose_name="Текст")
    created_at = models.DateTimeField(editable=False, verbose_name='Дата создания')

    class Meta:
        verbose_name = "Обратная связь"
        verbose_name_plural = "Обратная связь"
