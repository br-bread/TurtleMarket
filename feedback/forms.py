from django import forms

from .models import Feedback


class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = (Feedback.text.field.name,)
        labels = {
            Feedback.text.field.name: 'Отзыв',
        }
        widgets = {
            Feedback.text.field.name: forms.TextInput(
                attrs={'class': 'form-control'}),
        }
