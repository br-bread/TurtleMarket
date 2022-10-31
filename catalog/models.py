from django.core.validators import (MaxValueValidator, MinValueValidator,
                                    RegexValidator)
from django.db import models

from Core.models import BaseModel

from .validators import AmazingValidator


class Tag(BaseModel):
    name = models.CharField('Название', max_length=150,
                            help_text='Максимальная длина - 150 символов')
    is_published = models.BooleanField('Опубликовано', default=True)
    slug = models.CharField(max_length=200,
                            validators=[RegexValidator(regex='[a-zA-Z0-9_-]')])

    class Meta:
        verbose_name = 'Тег'
        verbose_name_plural = 'Теги'


class Category(BaseModel):
    name = models.CharField('Название', max_length=150,
                            help_text='Максимальная длина - 150 символов')
    is_published = models.BooleanField('Опубликовано', default=True)
    slug = models.CharField(max_length=200,
                            validators=[RegexValidator(regex='[a-zA-Z0-9_-]')])
    weight = models.IntegerField(
        default=100, validators=[MaxValueValidator(limit_value=32766),
                                 MinValueValidator(limit_value=1)])

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Item(BaseModel):
    name = models.CharField('Название', max_length=150,
                            help_text='Максимальная длина - 150 символов')
    is_published = models.BooleanField('Опубликовано', default=True)
    text = models.TextField(
        'Описание',
        validators=[
            AmazingValidator('превосходно', 'роскошно').call])
    category = models.ForeignKey(Category, on_delete=models.CASCADE,
                                 related_name='items')
    tags = models.ManyToManyField(Tag)

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'
