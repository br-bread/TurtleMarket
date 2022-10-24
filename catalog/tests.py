from django.test import Client, TestCase


class StaticURLTests(TestCase):
    def test_catalog_url(self):
        response = Client().get('/catalog/')
        self.assertEqual(response.status_code, 200, response.content)
        response = Client().get('/catalog/1/')
        self.assertEqual(response.status_code, 200)
        response = Client().get('/catalog/1-sdj/')
        self.assertNotEqual(response.status_code, 200)
        response = Client().get('/catalog/ghg/')
        self.assertNotEqual(response.status_code, 200)
        response = Client().get('/catalog/-3/')
        self.assertNotEqual(response.status_code, 200)
