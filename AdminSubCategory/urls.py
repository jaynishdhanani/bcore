from django.urls import path
from . import views


urlpatterns = [
    path('back/subcategory',views.customsubadmin),
    path('back/subcategory/add',views.addSubcategory),
    path('subcategory/delete/<int:id>',views.deleteSubCategory),
    path('subcategory/update/<int:id>',views.updateSubCategory),
]