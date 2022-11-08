from django.db import models
from django.utils.safestring import mark_safe
from django_quill.fields import QuillField
from sorl.thumbnail import get_thumbnail

from core.models import BaseModel

from .validators import amazing_validator


class Tag(BaseModel):
    slug = models.SlugField(max_length=200, help_text='Максимум 200 символов')

    class Meta:
        verbose_name = 'тег'
        verbose_name_plural = 'теги'

    def __str__(self):
        return self.name


class Category(BaseModel):
    slug = models.SlugField(max_length=200, help_text='Максимум 200 символов')
    weight = models.PositiveSmallIntegerField(default=100)

    class Meta:
        ordering = ('weight', 'id')
        verbose_name = 'категория'
        verbose_name_plural = 'категории'

    def __str__(self):
        return self.name


class Item(BaseModel):
    name = models.CharField('название',
                            max_length=150,
                            help_text='Максимальная длина - 150 символов',
                            unique=False)
    text = QuillField(
        'описание',
        validators=[amazing_validator('превосходно', 'роскошно')],
        help_text='Не забудьте указать роскошные и превосходные стороны')
    category = models.ForeignKey(Category,
                                 on_delete=models.CASCADE,
                                 verbose_name='категория')
    tags = models.ManyToManyField(Tag, verbose_name='тег')
    upload = models.ImageField('изображение',
                               upload_to='uploads/%m',
                               default=None)

    @property
    def get_img(self):
        return get_thumbnail(self.upload, '300x300', crop='center', quality=51)

    def image_tmb(self):
        if self.upload:
            return mark_safe(
                f'<img src="{self.get_img.url}">'
            )
        return "Нет изображения"

    image_tmb.short_description = 'превью'
    image_tmb.allow_tags = True

    class Meta:
        verbose_name = 'товар'
        verbose_name_plural = 'товары'
        default_related_name = 'items'

    def __str__(self):
        return self.name


class Gallery(models.Model):
    upload = models.ImageField('изображение')
    item = models.ForeignKey(Item,
                             on_delete=models.CASCADE,
                             verbose_name='товар')

    @property
    def get_img(self):
        return get_thumbnail(self.upload, '300x300', crop='center', quality=51)

    def image_tmb(self):
        if self.upload:
            return mark_safe(
                f'<img src="{self.get_img.url}">'
            )
        return "Нет изображения"

    image_tmb.short_description = 'изображение'
    image_tmb.allow_tags = True

    class Meta:
        verbose_name = 'фото товара'
        verbose_name_plural = 'фото товара'
        default_related_name = 'images'

    def __str__(self):
        return self.upload.url
