from django.db import models


class BaseModel(models.Model):
    name = models.CharField('название',
                            max_length=150,
                            help_text='Максимальная длина - 150 символов',
                            unique=True)
    is_published = models.BooleanField('опубликовано', default=True)

    class Meta:
        abstract = True
