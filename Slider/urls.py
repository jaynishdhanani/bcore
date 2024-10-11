from django.urls import path
from . import views


urlpatterns = [
    path('add/slider',views.SliderPage),
    path('view/slider',views.ViewSlider),
    path('slider/update/<int:id>',views.UpdateSlider),
    path('slider/delete/<int:id>',views.DeleteSlider),
]