from django.urls import path
from . import views


urlpatterns = [
    path('home',views.Homepage),
    path('about',views.AboutProduct),
    path('contact',views.ContactProduct),
    path('product/shop',views.ShopProduct),
    path('userprofile',views.UserProfile),
    path('user/login',views.UserLogin),
    path('createaccount',views.CreateAccount),
    path('product/info/<int:id>',views.InfoProduct),
    path('user/logout',views.UserLogout),
    path('category/by/products/<int:catid>',views.CategoryByProducts),
]