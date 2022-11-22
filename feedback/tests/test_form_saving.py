from django.core.exceptions import ValidationError
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
            test_feedback = Feedback(text=i)
            test_feedback.full_clean()
            test_feedback.save()
        self.assertEqual(feedback_count,
                         Feedback.objects.count() - len(test_texts))

    def test_creating_invalid_form(self):
        feedback_count = Feedback.objects.count()
        test_texts = ['', ' ', '  ']
        with self.assertRaises(ValidationError):
            for i in test_texts:
                test_feedback = Feedback(text=i)
                test_feedback.full_clean()
                test_feedback.save()
        self.assertEqual(feedback_count, Feedback.objects.count())
