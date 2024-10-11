from django.urls import path
from . import views


urlpatterns = [
    path('product/checkout',views.Checkoutpage),
    path('createOrder',views.createOrder),
]