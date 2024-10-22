from django.contrib import admin
from django.urls import path,include#
from . import views
urlpatterns = [
    path('api/getAllUser',views.getAllUser),
    path('api/getAllProducts',views.getAllProducts),
    path('api/getSingleProducts/<int:id>',views.getSingleProducts),
    path('api/getAllOrder',views.getAllOrder),
    path('api/getSingleOrder/<int:id>',views.getSingleOrder),
    path('api/getSingleItemProduct/<int:id>',views.getSingleItemProduct),
    path('api/UpdateOrder/<int:id>',views.UpdateOrder),
    path('api/login',views.UserLogin),
]