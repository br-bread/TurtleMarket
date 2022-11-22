from django import forms
from django.core.exceptions import ValidationError
from .models import Feedback


class FeedbackForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(FeedbackForm, self).__init__(*args, **kwargs)

    def clean_description(self):
        s = self.cleaned_data['text']
        if not s:
            raise ValidationError("Обязательное поле")
        return s

    class Meta:
        model = Feedback
        fields = (Feedback.text.field.name,)
        labels = {
            Feedback.text.field.name: 'Отзыв',
        }
        widgets = {
            Feedback.text.field.name: forms.TextInput(
                attrs={'class': 'form-control',
                       'required': True}),
        }
