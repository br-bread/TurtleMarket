from django.test import Client, TestCase


class StaticURLTests(TestCase):
    def test_homepage_url(self):
        response = Client().get('/')
        self.assertEqual(response.status_code, 200)
        response = Client().get('/homepage/')
        self.assertNotEqual(response.status_code, 200)
