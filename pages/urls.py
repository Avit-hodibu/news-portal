import imp
from turtle import home
from unicodedata import name
from django import urls
from django.urls import path
from .views import HomePageView

urlpatterns = [
    path('', HomePageView.as_view(), name='home')
]
