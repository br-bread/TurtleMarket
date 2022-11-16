from django.test import Client, TestCase
from django.urls import reverse


class StaticURLTests(TestCase):
    def test_main_catalog_url(self):
        response = Client().get(reverse('catalog:item_list'))
        self.assertEqual(response.status_code, 200)

    def test_correct_catalog_url(self):
        tests = [{'url': '1/', 'expected_response': 404},
                 {'url': '123/', 'expected_response': 404}]

        for i in range(len(tests)):
            response = Client().get(reverse('catalog:item_detail',
                                            kwargs={'pk': tests[i]['url']}))
            with self.subTest(f'{tests[i]["url"][:-1]}'
                              ' is a positive integer', i=i):
                self.assertEqual(response.status_code,
                                 tests[i]['expected_response'])

    def test_wrong_catalog_url(self):
        tests = ['0', '-1', '0123', 'a', '1a', '1a2', 'a1',
                 'one', '_-', '_1', '1_3', '123_', '1/12']

        for i in range(len(tests)):
            response = Client().get(reverse('catalog:item_detail',
                                            kwargs={'pk': tests[i] + '/'}))
            with self.subTest(f'{tests[i][:]} is not a positive integer', i=i):
                self.assertNotEqual(response.status_code, 200)
