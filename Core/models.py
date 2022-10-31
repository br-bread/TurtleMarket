from statistics import mode

from django.db import models


class BaseModel(models.Model):
    name = models.CharField()
    is_published = models.BooleanField()

    class Meta:
        abstract = True
