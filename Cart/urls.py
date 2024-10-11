from django.urls import path
from . import views


urlpatterns = [
    path('addtocart',views.addtocart),
    path('addtocartsingle/<int:pid>',views.addtocartsingle),
    path('product/cart',views.CartProduct),
    path('product/cart/<int:id>',views.deleteCart),
    path('getAllCart',views.getAllCart),
]