from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from . import views

app_name = 'users'
urlpatterns = [
    path('signup/', views.sign_up, name='sign_up'),
    path('profile/', views.profile, name='profile'),
    path('user_list/', views.user_list, name='user_list'),
    path('user_detail/', views.user_detail, name='user_detail'),

    path('login/',
         LoginView.as_view(template_name='users/login.html'),
         name='login'),

    path('logout/',
         LogoutView.as_view(template_name='users/logout.html'),
         name='logout'),
]
