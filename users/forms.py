from django import forms
from django.core.exceptions import ValidationError

from .models import Profile, User


class SignupForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(SignupForm, self).__init__(*args, **kwargs)
        self.fields['password_confirm'] = forms.CharField(
            max_length=128,
            required=True,
            label='Подтвердите пароль',
            widget=forms.PasswordInput(attrs={
                                       'class': 'form-control',
                                       'required': True})
        )

    class Meta:
        model = User
        login = User.login.field.name
        mail = User.email.field.name
        password = User.password.field.name

        fields = (mail, login, password)

        labels = {
            mail: 'Электронная почта',
            login: 'Логин',
            password: 'Пароль',
        }

        widgets = {
            mail: forms.EmailInput(
                attrs={'class': 'form-control',
                       'required': True}),
            login: forms.TextInput(
                attrs={'class': 'form-control',
                       'required': True}),
            password: forms.PasswordInput(
                attrs={'class': 'form-control',
                       'required': True}),
        }

    error_messages = {
        'password_mismatch': 'Пароли не совпадают',
    }

    def clean_password_confirm(self):
        cleaned_data = super(SignupForm, self).clean()
        password = cleaned_data.get("password")
        password_confirm = cleaned_data.get("password_confirm")

        if password != password_confirm:
            raise forms.ValidationError(
                self.error_messages['password_mismatch'],
                code='password_mismatch',
            )
        return cleaned_data


class UserForm(forms.ModelForm):

    class Meta:
        model = User
        login = User.login.field.name
        mail = User.email.field.name

        fields = (mail, login)
        labels = {
            mail: 'Электронная почта',
            login: 'Логин',
        }

        widgets = {
            mail: forms.EmailInput(
                attrs={'class': 'form-control',
                       'required': True}),
            login: forms.TextInput(
                attrs={'class': 'form-control',
                       'required': True}),
        }


class ProfileForm(forms.ModelForm):

    class Meta:
        model = Profile
        birthday = Profile.birthday.field.name

        fields = (birthday,)
        labels = {
            birthday: 'День рождения',
        }
        widgets = {
            birthday: forms.DateInput(
                attrs={'class': 'form-control',
                       'required': True}),
        }
