from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('AdminDashboard.urls')),
    path('',include('AdminCategory.urls')),
    path('',include('AdminSubCategory.urls')),
    path('',include('AdminProduct.urls')),
    path('',include('AdminState.urls')),
    path('',include('AdminCity.urls')),
    path('',include('Home.urls')),
    path('',include('Cart.urls')),
    path('',include('Checkout.urls')),
    path('',include('Order.urls')),
    path('',include('Items.urls')),
    path('',include('ChangePassword.urls')),
    path('',include('Slider.urls')),
    path('',include('MyEmail.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)