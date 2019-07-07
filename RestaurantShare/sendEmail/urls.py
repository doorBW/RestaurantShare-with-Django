# sendEmail > urls.py
from django.urls import path, include
from . import views

urlpatterns = [
    path('send/', views.sendEmail)
]