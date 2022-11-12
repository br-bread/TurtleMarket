from django.contrib import admin
from django.db import models
from django.utils.safestring import mark_safe
from django_quill.fields import QuillField

from core.models import BaseImageModel, BaseModel

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

    def image_tmb(self):
        if self.main_image.upload:
            return mark_safe(
                f'<img src="{self.main_image.get_img_50x50.url}">'
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


class MainImage(BaseImageModel):
    item = models.OneToOneField(Item,
                                on_delete=models.CASCADE,
                                verbose_name='товар',
                                related_name='main_image')

    def image_tmb(self):
        return super().image_tmb()

    image_tmb.short_description = 'превью'

    class Meta:
        verbose_name = 'превью товара'
        verbose_name_plural = 'превью товара'


class GalleryImage(BaseImageModel):
    item = models.ForeignKey(Item,
                             on_delete=models.CASCADE,
                             verbose_name='товар',
                             related_name='gallery_images')

    def image_tmb(self):
        return super().image_tmb()

    image_tmb.short_description = 'изображение'

    class Meta:
        verbose_name = 'фото товара'
        verbose_name_plural = 'фото товара'
