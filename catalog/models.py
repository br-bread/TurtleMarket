from django.db import models

from core.models import BaseModel

from .validators import AmazingValidator


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
    text = models.TextField(
        'описание',
        validators=[AmazingValidator('превосходно', 'роскошно')],
        help_text='Не забудьте указать роскошные и превосходные стороны')
    category = models.ForeignKey(Category,
                                 on_delete=models.CASCADE,
                                 verbose_name='категория')
    tags = models.ManyToManyField(Tag, verbose_name='тег')

    class Meta:
        verbose_name = 'товар'
        verbose_name_plural = 'товары'
        default_related_name = 'items'

    def __str__(self):
        return self.name
