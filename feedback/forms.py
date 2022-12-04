from django import forms
from django.core.exceptions import ValidationError

from .models import Feedback


class FeedbackForm(forms.ModelForm):
    error_messages = {
        'required': 'Поле не может быть пустым',
    }

    def clean_text(self):
        cleaned_data = super(FeedbackForm, self).clean()
        text = self.cleaned_data['text'].replace(' ', '')
        if not text:
            raise ValidationError(
                self.error_messages['required'],
                code='required',)
        return cleaned_data

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
