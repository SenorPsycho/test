from django.contrib import admin
from django.urls import path

from DjangoDay2 import views

urlpatterns = [
    path('home/', views.home),
]
