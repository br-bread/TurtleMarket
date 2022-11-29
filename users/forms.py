from django import forms

from .models import User


class SignupForm(forms.ModelForm):

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

        def clean(self):
            cleaned_data = super(SignupForm, self).clean()
            password = cleaned_data.get("password")
            password_confirm = cleaned_data.get("password_confirm")

            if password != password_confirm:
                self.add_error('password_confirm', "Пароли не совпадают")
                raise forms.ValidationError(
                    "password and confirm_password does not match"
                )

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
