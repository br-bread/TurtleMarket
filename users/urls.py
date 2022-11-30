from django.contrib.auth.views import (LoginView, LogoutView,
                                       PasswordChangeDoneView,
                                       PasswordChangeView)

from django.urls import path, re_path

from . import views

app_name = 'users'
urlpatterns = [
    path('signup/', views.sign_up, name='sign_up'),
    path('profile/', views.profile, name='profile'),
    path('user_list/', views.user_list, name='user_list'),
    re_path('user_detail/(?P<pk>[1-9]\\d*)/$',
            views.user_detail,
            name='user_detail'),

    path('login/',
         LoginView.as_view(template_name='users/login.html'),
         name='login'),

    path('logout/',
         LogoutView.as_view(template_name='users/logout.html'),
         name='logout'),

    path('change_password/',
         PasswordChangeView.as_view(
             template_name='users/change_password.html'),
         name='change_password'),
    path('password_change/done/',
         PasswordChangeDoneView.as_view(
             template_name='users/change_password_complete.html'),
         name='change_password_complete'),
]
