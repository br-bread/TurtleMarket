from django.core.validators import (MaxValueValidator, MinValueValidator,
                                    RegexValidator)
from django.db import models

from Core.models import BaseModel

from .validators import AmazingValidator


class Tag(BaseModel):
    name = models.CharField('Название', max_length=150,
                            help_text='Максимальная длина - 150 символов')
    is_published = models.BooleanField('Опубликовано', default=True)
    slug = models.SlugField(max_length=200)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Тег'
        verbose_name_plural = 'Теги'


class Category(BaseModel):
    name = models.CharField('Название', max_length=150,
                            help_text='Максимальная длина - 150 символов')
    is_published = models.BooleanField('Опубликовано', default=True)
    slug = models.SlugField(max_length=200)
    weight = models.PositiveSmallIntegerField(default=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Item(BaseModel):
    name = models.CharField('Название', max_length=150,
                            help_text='Максимальная длина - 150 символов')
    is_published = models.BooleanField('Опубликовано', default=True)
    text = models.TextField(
        'Описание',
        validators=[AmazingValidator('прекрасно', 'роскошно')])
    category = models.ForeignKey(Category, on_delete=models.CASCADE,
                                 related_name='items')
    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'
