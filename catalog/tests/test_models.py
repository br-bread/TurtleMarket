import json

from django.core.exceptions import ValidationError
from django.test import TestCase

from catalog.models import Category, Item, Tag


class ModelItemTest(TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.item_category = Category.objects.create(name='test_category',
                                                    slug='test_category_slug',
                                                    weight=100)
        cls.item_tag = Tag.objects.create(name='test_tag',
                                          slug='test_tag_slug')

    def test_amazing_validator_correct(self):
        item_count = Item.objects.count()
        item_texts = ['превосходно роскошно', 'ПрЕвосХОДно', 'Роскошно!',
                      'Не превосходно', 'Потрясающе(превосходно)',
                      'Замечательно! Превосходно!']
        for i in range(len(item_texts)):
            text_dict = dict()
            text_dict['delta'] = ''
            text_dict['html'] = f'<p>{item_texts[i]}</p>'
            json_text = json.dumps(text_dict)
            new_item = Item(name=f'test_item{i}',
                            text=json_text,
                            category=self.item_category)
            new_item.full_clean()
            new_item.save()
            new_item.tags.add(self.item_tag)

        self.assertEqual(item_count, Item.objects.count() - len(item_texts))

    def test_amazing_validator_wrong(self):
        item_count = Item.objects.count()
        with self.assertRaises(ValidationError):
            item_texts = ['Прекрасно', 'пре восход но',
                          '1234', 'Препревосходно123']
            for i in range(len(item_texts)):
                text_dict = dict()
                text_dict['delta'] = ''
                text_dict['html'] = f'<p>{item_texts[i]}</p>'
                json_text = json.dumps(text_dict)
                new_item = Item(name='name',
                                is_published=1,
                                text=json_text,
                                category=self.item_category)
                new_item.full_clean()
                new_item.save()
                new_item.tags.add(self.item_tag)

        self.assertEqual(item_count, Item.objects.count())
