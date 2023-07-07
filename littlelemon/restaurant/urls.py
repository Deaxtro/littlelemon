from django.urls import path
from .views import *

urlpatterns = [
    path('',indexview, name='index'),
    path('menu/', MenuItemView.as_view(),name='menu'),
    path('menu/<int:pk>', SingleMenuItemView.as_view()),
]