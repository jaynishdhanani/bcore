from django.urls import path
from . import views


urlpatterns = [
    path('product/order',views.Orderinfo),
]