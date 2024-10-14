from django.contrib import admin
from django.urls import path,include#
from . import views
urlpatterns = [
    path('api/getAllProducts',views.getAllProducts),
    path('api/getSingleProducts/<int:id>',views.getSingleProducts),
]