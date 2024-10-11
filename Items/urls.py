from django.urls import path
from . import views


urlpatterns = [
    path('product/items/<int:id>',views.ProductItems),
]