from django.urls import path
from . import views


urlpatterns = [
    path('back/city',views.customcity),
    path('back/city/add',views.AddCity),
    path('city/delete/<int:id>',views.deleteCity),
    path('city/update/<int:id>',views.updateCity),
    path('loadcitybystate',views.loadcitybystate),
    path('loadcitydata',views.loadcitydata),
]