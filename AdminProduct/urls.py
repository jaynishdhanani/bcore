from django.urls import path
from . import views


urlpatterns = [
    path('back/product',views.adminproduct),
    path('back/product/add',views.addProduct),
    path('product/delete/<int:id>',views.deleteProduct),
    path('product/update/<int:id>',views.updateProduct),
    path('changeStatus/<int:id>/<str:status>',views.changeStatus),
]