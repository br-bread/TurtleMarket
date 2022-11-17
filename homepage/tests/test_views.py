import json

from django.test import Client, TestCase
from django.urls import reverse

from catalog.models import Item


class TaskPagesTest(TestCase):
    def test_homepage_show_correct_context(self):
        response = Client().get(reverse('homepage:home'))
        self.assertIn('items', response.context)
        self.assertEqual(len(response.context['items']), Item.objects.count())
