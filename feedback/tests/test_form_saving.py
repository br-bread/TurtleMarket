from django.test import TestCase

from feedback.forms import FeedbackForm
from feedback.models import Feedback


class FormSavingTests(TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.form = FeedbackForm()

    def test_creating_valid_form(self):
        feedback_count = Feedback.objects.count()
        test_texts = ['Nice!', 'i love turtles', 'cherepashka']
        for i in test_texts:
            test_feedback = Feedback.objects.create(name='test_name',
                                                    mail='test@test.com',
                                                    text=i)
            test_feedback.full_clean()
        self.assertEqual(feedback_count + len(test_texts),
                         Feedback.objects.count())
