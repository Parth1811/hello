from django.db import models
from django.contrib.postgres.fields import IntegerRangeField


class Article(models.Model):

    LTE_50 = (1, 50)
    LTE_100 = (51, 100)

    SIZE_CHOICES = [
        (LTE_50, "1-50"),
        (LTE_100, "51-100"),
    ]

    article_size = IntegerRangeField()

    class Meta:
        verbose_name = "Article"
        verbose_name_plural = "Articles"

    def __str__(self):
        return "test"
