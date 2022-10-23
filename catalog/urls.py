
from django.urls import path, re_path

from . import views

urlpatterns = [
    path('', views.item_list),
    re_path('(?P<pk>\\d+)/', views.item_detail),
]
