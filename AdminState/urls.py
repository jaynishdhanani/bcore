from django.urls import path
from . import views


urlpatterns = [
    path('back/state',views.customstate),
    path('back/state/add',views.AddState),
    path('state/delete/<int:id>',views.deleteState),
    path('state/update/<int:id>',views.updateState),
]