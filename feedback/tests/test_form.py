from django.test import Client, TestCase
from feedback.forms import FeedbackForm
from django.urls import reverse


class FormTests(TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.form = FeedbackForm()

    def test_form_in_context(self):
        response = Client().get(reverse('feedback:feedback'))
        self.assertIn('form', response.context)

    def test_text_label(self):
        text_label = FormTests.form.fields['text'].label
        self.assertEqual(text_label, 'Отзыв')

    def test_text_help_text(self):
        text_help_text = FormTests.form.fields['text'].help_text
        self.assertEqual(text_help_text, 'Максимальная длина 300 символов')

    def test_redirect(self):
        form_data = {
            'text': 'test_text'
        }
        response = Client().post(reverse('feedback:feedback'),
                                 data=form_data,
                                 follow=True)
        self.assertRedirects(response, reverse('feedback:feedback'))
