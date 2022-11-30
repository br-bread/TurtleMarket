from django.contrib.auth.views import (LoginView, LogoutView,
                                       PasswordChangeDoneView,
                                       PasswordChangeView,
                                       PasswordResetCompleteView,
                                       PasswordResetConfirmView,
                                       PasswordResetDoneView,
                                       PasswordResetView)
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
             template_name='users/password/change_password.html'),
         name='change_password'),
    path('password_change/done/',
         PasswordChangeDoneView.as_view(
             template_name='users/password/change_password_complete.html'),
         name='change_password_complete'),
    path('password_reset',
         PasswordResetView.as_view(
             template_name='users/password/password_reset.html'),
         name='password_reset'),
    path('password_reset/done/',
         PasswordResetDoneView.as_view(
             template_name='users/password/password_reset_done.html'
         ),
         name='password_reset_done'),
    re_path('^reset/(?P<uidb64>[0-9A-Za-z_\\-]+)/(?P<token>.+)/$',
            PasswordResetConfirmView.as_view(
                template_name='users/password/password_reset_confirm.html'
            ),
            name='password_reset_confirm'),
    path('reset/done/',
         PasswordResetCompleteView.as_view(
             template_name='users/password/password_reset_complete.html'
         ),
         name='password_reset_complete'),
]
