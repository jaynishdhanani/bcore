from django.urls import path
from . import views


urlpatterns = [
    path('view/employee',views.ViewEmployee),
    path('add/employee',views.AddEmployee),
]