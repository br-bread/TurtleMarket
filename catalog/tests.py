from django.test import Client, TestCase


class StaticURLTests(TestCase):
    def test_main_catalog_url(self):
        response = Client().get('/catalog/')
        self.assertEqual(response.status_code, 200)

    def test_correct_catalog_url(self):
        tests = ['1/', '123/']

        for i in range(len(tests)):
            response = Client().get('/catalog/' + tests[i])
            with self.subTest(f'{tests[i][:-1]} is a positive integer', i=i):
                self.assertEqual(response.status_code, 200)

    def test_wrong_catalog_url(self):
        tests = ['0', '-1', '0123', 'a', '1a', '1a2', 'a1',
                 'one', '_-', '_1', '1_3', '123_', '1/12']

        for i in range(len(tests)):
            response = Client().get('/catalog/' + tests[i] + '/')
            with self.subTest(f'{tests[i][:]} is not a positive integer', i=i):
                self.assertNotEqual(response.status_code, 200)
