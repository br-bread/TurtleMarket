from django.shortcuts import get_object_or_404, redirect, render

from . import forms
from .models import User


def sign_up(request):
    template_name = 'users/signup.html'
    form = forms.SignupForm(request.POST or None)
    context = {
        'form': form,
    }

    if request.method == 'POST' and form.is_valid():
        login = form.cleaned_data['login']
        mail = form.cleaned_data['email']
        password = form.cleaned_data['password']

        User.objects.create_user(mail, login, password)
        return redirect('users:profile')

    return render(request, template_name, context)


def profile(request):
    template_name = 'users/profile.html'
    form = 1
    context = {
        'form': form,
    }

    return render(request, template_name, context)


def user_list(request):
    template_name = 'users/user_list.html'
    users = User.objects.only('login')
    context = {
        'users': users,
    }
    return render(request, template_name, context)


def user_detail(request, pk):
    template_name = 'users/user_detail.html'
    user = get_object_or_404(
        User.objects.only('login', 'mail'), pk=pk)

    context = {
        'user': user,
    }
    return render(request, template_name, context)


def handler404(request, exception, template_name="error_404.html"):
    response = render(request, template_name)
    response.status_code = 404
    return response
