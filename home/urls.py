from django.contrib import admin
from django.urls import path
from . import views

# Home URL
urlpatterns = [
    path('', views.index, name='home')
]
