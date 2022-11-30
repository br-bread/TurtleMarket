from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render

from . import forms
from .models import Profile, User


def sign_up(request):
    if request.user is not None:
        return redirect('users:profile')
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


@login_required
def profile(request):
    template_name = 'users/profile.html'
    user = request.user
    userform = forms.UserForm(request.POST or None,
                              initial={'login': user.login,
                                       'email': user.email})
    profileform = forms.ProfileForm(
        request.POST or None,
        initial={'birthday': user.profile.birthday})
    context = {
        'userform': userform,
        'profileform': profileform,
    }

    if request.method == 'POST':
        if userform.is_valid():
            login = userform.cleaned_data['login']
            email = userform.cleaned_data['email']
            user = User.objects.get(pk=user.id)
            user.login = login
            user.email = email
            user.save()
        if profileform.is_valid():
            birthday = profileform.cleaned_data['birthday']
            profile = Profile.objects.get(pk=user.id)
            profile.birthday = birthday
            profile.save()

        return redirect('users:profile')

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
        User.objects.only('login', 'email'), pk=pk)

    context = {
        'user': user,
    }
    return render(request, template_name, context)


def handler404(request, exception, template_name="error_404.html"):
    response = render(request, template_name)
    response.status_code = 404
    return response
