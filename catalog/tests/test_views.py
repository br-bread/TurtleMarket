import json

from django.test import Client, TestCase
from django.urls import reverse

from catalog.models import Category, Item, Tag


class TaskPagesTest(TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.item_category = Category.objects.create(name='test_category',
                                                    slug='test_category_slug',
                                                    weight=100)
        cls.item_tag = Tag.objects.create(name='test_tag',
                                          slug='test_tag_slug')

    def test_homepage_show_correct_context(self):
        response = Client().get(reverse('homepage:home'))
        self.assertIn('items', response.context)
        self.assertEqual(len(response.context['items']), Item.objects.count())

    def test_catalog_itemlist_show_correct_context(self):
        response = Client().get(reverse('catalog:item_list'))
        self.assertIn('items', response.context)
        self.assertEqual(len(response.context['items']), Item.objects.count())

    def test_catalog_item_detail_show_correct_context(self):
        text_dict = dict()
        text_dict["delta"] = "{\"ops\":[{\"insert\":\"" + \
                             'роскошно' + "\\n\"}]}"
        text_dict["html"] = "<p>роскошно</p>"
        json_text = json.dumps(text_dict)
        new_item = Item(name='test_item1',
                        text=json_text,
                        category=self.item_category)
        new_item.full_clean()
        new_item.save()
        new_item.tags.add(self.item_tag)
        response = Client().get(reverse('catalog:item_detail',
                                        kwargs={'pk': 1}))
        self.assertIn('item', response.context)
