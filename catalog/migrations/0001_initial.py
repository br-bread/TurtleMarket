# Generated by Django 3.2.16 on 2022-10-31 00:37

import catalog.validators
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Максимальная длина - 150 символов', max_length=150, verbose_name='Название')),
                ('is_published', models.BooleanField(default=True, verbose_name='Опубликовано')),
                ('slug', models.CharField(max_length=200, validators=[django.core.validators.RegexValidator(regex='[a-zA-Z0-9_-]')])),
                ('weight', models.IntegerField(default=100, validators=[django.core.validators.MaxValueValidator(limit_value=32766), django.core.validators.MinValueValidator(limit_value=1)])),
            ],
            options={
                'verbose_name': 'Категория',
                'verbose_name_plural': 'Категории',
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Максимальная длина - 150 символов', max_length=150, verbose_name='Название')),
                ('is_published', models.BooleanField(default=True, verbose_name='Опубликовано')),
                ('slug', models.CharField(max_length=200, validators=[django.core.validators.RegexValidator(regex='[a-zA-Z0-9_-]')])),
            ],
            options={
                'verbose_name': 'Тег',
                'verbose_name_plural': 'Теги',
            },
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Максимальная длина - 150 символов', max_length=150, verbose_name='Название')),
                ('is_published', models.BooleanField(default=True, verbose_name='Опубликовано')),
                ('text', models.TextField(validators=[catalog.validators.AmazingValidator.call], verbose_name='Описание')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to='catalog.category')),
                ('tags', models.ManyToManyField(to='catalog.Tag')),
            ],
            options={
                'verbose_name': 'Товар',
                'verbose_name_plural': 'Товары',
            },
        ),
    ]
