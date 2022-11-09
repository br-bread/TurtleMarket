from django.db import models
from sorl.thumbnail import get_thumbnail


class BaseModel(models.Model):
    name = models.CharField('название',
                            max_length=150,
                            help_text='Максимальная длина - 150 символов',
                            unique=True)
    is_published = models.BooleanField('опубликовано', default=True)

    class Meta:
        abstract = True


class BaseImageModel(models.Model):
    upload = models.ImageField('изображение',
                               upload_to='uploads/',
                               null=True)

    @property
    def get_img(self):
        return get_thumbnail(self.upload, '300x300', crop='center', quality=51)

    class Meta:
        abstract = True
