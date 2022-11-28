# Generated by Django 3.2.16 on 2022-11-28 21:35

import django.db.models.deletion
import django_quill.fields
from django.db import migrations, models

import catalog.validators


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(help_text='Максимум 200 символов', max_length=200)),
                ('name', models.CharField(help_text='Максимальная длина - 150 символов', max_length=150, unique=True, verbose_name='название')),
                ('is_published', models.BooleanField(default=True, verbose_name='опубликовано')),
                ('weight', models.PositiveSmallIntegerField(default=100)),
            ],
            options={
                'verbose_name': 'категория',
                'verbose_name_plural': 'категории',
                'ordering': ('weight', 'id'),
            },
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_published', models.BooleanField(default=True, verbose_name='опубликовано')),
                ('name', models.CharField(help_text='Максимальная длина - 150 символов', max_length=150, verbose_name='название')),
                ('is_on_main', models.BooleanField(default=False, help_text='Отображается ли в списке товаров на главной странице', verbose_name='на главной')),
                ('text', django_quill.fields.QuillField(help_text='Не забудьте указать роскошные и превосходные стороны', validators=[catalog.validators.amazing_validator], verbose_name='описание')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to='catalog.category', verbose_name='категория')),
            ],
            options={
                'verbose_name': 'товар',
                'verbose_name_plural': 'товары',
                'default_related_name': 'items',
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(help_text='Максимум 200 символов', max_length=200)),
                ('name', models.CharField(help_text='Максимальная длина - 150 символов', max_length=150, unique=True, verbose_name='название')),
                ('is_published', models.BooleanField(default=True, verbose_name='опубликовано')),
            ],
            options={
                'verbose_name': 'тег',
                'verbose_name_plural': 'теги',
            },
        ),
        migrations.CreateModel(
            name='MainImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('upload', models.ImageField(null=True, upload_to='uploads/', verbose_name='изображение')),
                ('item', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='main_image', to='catalog.item', verbose_name='товар')),
            ],
            options={
                'verbose_name': 'превью товара',
                'verbose_name_plural': 'превью товара',
            },
        ),
        migrations.AddField(
            model_name='item',
            name='tags',
            field=models.ManyToManyField(related_name='items', to='catalog.Tag', verbose_name='тег'),
        ),
        migrations.CreateModel(
            name='GalleryImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('upload', models.ImageField(null=True, upload_to='uploads/', verbose_name='изображение')),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='gallery_images', to='catalog.item', verbose_name='товар')),
            ],
            options={
                'verbose_name': 'фото товара',
                'verbose_name_plural': 'фото товара',
            },
        ),
    ]
