from django.contrib import admin
from django.urls import path
from .import views

urlpatterns = [
    path('send/email',views.SendEmail),
] 