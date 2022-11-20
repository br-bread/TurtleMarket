from django import forms

from .models import Feedback


class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = (Feedback.text.field.name,)
        labels = {
            Feedback.text.field.name: 'текст',
        }
        help_texts = {
            Feedback.text.field.name: 'алё',
        }