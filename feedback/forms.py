from django import forms
from django.core.exceptions import ValidationError

from .models import Feedback


class FeedbackForm(forms.ModelForm):
    def clean_text(self):
        s = self.cleaned_data['text'].replace(' ', '')
        if not s:
            raise ValidationError("Обязательное поле")
        return s

    class Meta:
        model = Feedback
        name = Feedback.name.field.name
        mail = Feedback.mail.field.name
        text = Feedback.text.field.name
        fields = (name, mail, text)
        labels = {
            name: 'Имя',
            mail: 'Почта',
            text: 'Отзыв',
        }
        widgets = {
            name: forms.TextInput(
                attrs={'class': 'form-control',
                       'required': True}),
            mail: forms.TextInput(
                attrs={'class': 'form-control',
                       'required': True}),
            text: forms.TextInput(
                attrs={'class': 'form-control',
                       'required': True}),
        }
