from django.urls import path
from . import views


urlpatterns = [
    path('back/dashboard',views.dashboard),

]