from django.db import models
from django.utils.safestring import mark_safe
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
    def get_img_300x300(self):
        return get_thumbnail(self.upload, '300x300', crop='center', quality=51)

    @property
    def get_img_50x50(self):
        return get_thumbnail(self.upload, '50x50', crop='center', quality=51)

    def image_tmb(self):
        if self.upload:
            return mark_safe(
                f'<img src="{self.get_img_300x300.url}">'
            )
        return "Нет изображения"

    image_tmb.allow_tags = True

    class Meta:
        abstract = True

    def __str__(self):
        return self.upload.url
