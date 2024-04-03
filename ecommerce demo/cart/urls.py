"""
URL configuration for ecommerce project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from cart import views
app_name="cart"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('addcart/<int:p>',views.addcart,name='addcart'),
    path('cartview/',views.cartview,name='cartview'),
    path('remove/<int:p>',views.remove,name='remove'),
    path('delete/<int:p>', views.full_remove, name='delete'),
    path('order',views.orderform,name='order'),
    path('orderdetails',views.orderdetails, name='orderdetails'),
    path('orders/',views.yourorder,name='orders'),
]
