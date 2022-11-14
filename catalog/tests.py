import json

from django.core.exceptions import ValidationError
from django.test import Client, TestCase

from .models import Category, Item, Tag


class StaticURLTests(TestCase):
    def test_main_catalog_url(self):
        response = Client().get('/catalog/')
        self.assertEqual(response.status_code, 200)

    def test_correct_catalog_url(self):
        tests = [{'url': '1/', 'expected_response': 404},
                 {'url': '123/', 'expected_response': 404}]

        for i in range(len(tests)):
            response = Client().get('/catalog/' + tests[i]['url'])
            with self.subTest(f'{tests[i]["url"][:-1]}'
                              ' is a positive integer', i=i):
                self.assertEqual(response.status_code,
                                 tests[i]['expected_response'])

    def test_wrong_catalog_url(self):
        tests = ['0', '-1', '0123', 'a', '1a', '1a2', 'a1',
                 'one', '_-', '_1', '1_3', '123_', '1/12']

        for i in range(len(tests)):
            response = Client().get('/catalog/' + tests[i] + '/')
            with self.subTest(f'{tests[i][:]} is not a positive integer', i=i):
                self.assertNotEqual(response.status_code, 200)


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
            text_dict["delta"] = "{\"ops\":[{\"insert\":\"" + item_texts[i] + \
                                 "\\n\"}]}"
            text_dict["html"] = f"<p>{item_texts[i]}</p>"
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
                text_dict["delta"] = "{\"ops\":[{\"insert\":\"" + \
                                     item_texts[i] + "\\n\"}]}"
                text_dict["html"] = f"<p>{item_texts[i]}</p>"
                json_text = json.dumps(text_dict)
                new_item = Item(name='name',
                                is_published=1,
                                text=json_text,
                                category=self.item_category)
                new_item.full_clean()
                new_item.save()
                new_item.tags.add(self.item_tag)

        self.assertEqual(item_count, Item.objects.count())
