from django.core.validators import (MaxValueValidator, MinValueValidator,
                                    RegexValidator)
from django.db import models

from .validators import AmazingValidator


class Item(models.Model):
    name = models.CharField(max_length=150)
    is_published = models.BooleanField(default=True)
    text = models.TextField(validators=[AmazingValidator('превосходно',
                                                         'роскошно').call])


class Tag(models.Model):
    name = models.CharField(max_length=150)
    is_published = models.BooleanField(default=True)
    slug = models.CharField(max_length=200,
                            validators=[RegexValidator(regex='[a-zA-Z0-9_-]')])


class Category(models.Model):
    name = models.CharField(max_length=150)
    is_published = models.BooleanField(default=True)
    slug = models.CharField(max_length=200,
                            validators=[RegexValidator(regex='[a-zA-Z0-9_-]')])
    weight = models.IntegerField(
        default=100, validators=[MaxValueValidator(limit_value=32766),
                                 MinValueValidator(limit_value=1)])
