from django.urls import path
from . import views


urlpatterns = [
    path('changepassword',views.ChangePass),
]