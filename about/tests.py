from django.test import Client, TestCase


class StaticURLTests(TestCase):
    def test_about_url(self):
        response = Client().get('/about/')
        self.assertEqual(response.status_code, 200)
        response = Client().get('/about/1/')
        self.assertNotEqual(response.status_code, 200)
        response = Client().get('/about/h/')
        self.assertNotEqual(response.status_code, 200)
        response = Client().get('/about1/')
        self.assertNotEqual(response.status_code, 200)
