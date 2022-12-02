from django.contrib import admin
from django.db import models
from django.db.models import Prefetch
from django.utils.safestring import mark_safe
from django_quill.fields import QuillField

from core.models import BaseImageModel, BaseModel, SluggedModel

from .validators import amazing_validator


class Tag(BaseModel, SluggedModel):
    class Meta:
        verbose_name = 'тег'
        verbose_name_plural = 'теги'


class Category(BaseModel, SluggedModel):
    weight = models.PositiveSmallIntegerField(default=100)

    class Meta:
        ordering = ('weight', 'id')
        verbose_name = 'категория'
        verbose_name_plural = 'категории'


class ItemManager(models.Manager):
    def published(self):
        return (
            self.get_queryset()
            .select_related('category')
            .select_related('main_image')
            .prefetch_related(Prefetch('tags',
                              queryset=Tag.objects.filter(is_published=True)
                                                  .only('name')))
            .filter(is_published=True, category__is_published=True)
            .order_by('name')
            .only('name', 'text', 'category__name')
        )


class Item(BaseModel):
    objects = ItemManager()
    name = models.CharField('название',
                            max_length=150,
                            help_text='Максимальная длина 150 символов',
                            unique=False)
    is_on_main = models.BooleanField('на главной',
                                     default=False,
                                     help_text='Отображается ли в списке '
                                     'товаров на главной странице',)
    text = QuillField(
        'описание',
        validators=[amazing_validator('превосходно', 'роскошно')],
        help_text='Не забудьте указать роскошные и превосходные стороны')
    category = models.ForeignKey(Category,
                                 on_delete=models.CASCADE,
                                 verbose_name='категория')
    tags = models.ManyToManyField(Tag, verbose_name='тег')

    class Meta:
        verbose_name = 'товар'
        verbose_name_plural = 'товары'
        default_related_name = 'items'

    def image_tmb(self):
        if self.main_image.upload:
            return mark_safe(
                f'<img src="{self.main_image.get_img_300x300.url}">'
            )
        return "Нет изображения"

    def image_tmb_admin(self):
        if self.main_image.upload:
            return mark_safe(
                f'<img src="{self.main_image.get_img_50x50.url}">'
            )
        return "Нет изображения"

    image_tmb.short_description = 'превью'
    image_tmb.allow_tags = True
    image_tmb_admin.short_description = 'превью'
    image_tmb_admin.allow_tags = True


class MainImage(BaseImageModel):
    item = models.OneToOneField(Item,
                                on_delete=models.CASCADE,
                                verbose_name='товар',
                                related_name='main_image')

    class Meta:
        verbose_name = 'превью товара'
        verbose_name_plural = 'превью товара'

    def image_tmb(self):
        return super().image_tmb()

    image_tmb.short_description = 'превью'


class GalleryImage(BaseImageModel):
    item = models.ForeignKey(Item,
                             on_delete=models.CASCADE,
                             verbose_name='товар',
                             related_name='gallery_images')

    class Meta:
        verbose_name = 'фото товара'
        verbose_name_plural = 'фото товара'

    def image_tmb(self):
        return super().image_tmb()

    image_tmb.short_description = 'изображение'
