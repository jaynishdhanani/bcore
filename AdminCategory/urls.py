from django.urls import path
from . import views


urlpatterns = [
    path('back/category',views.customadmin),
    path('back/category/add',views.AddCategory),
    path('category/delete/<int:id>',views.deleteCategory),
    path('category/update/<int:id>',views.updateCategory),
]