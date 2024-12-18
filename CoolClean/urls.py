"""
URL configuration for CoolClean project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.urls import path, include
from CoolClean import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='home-page'),
    path('fridges/', include('CoolClean.fridges.urls')),
    path('washers/', include('CoolClean.washers.urls')),
    path('goods-sold/', include('CoolClean.goods_sold.urls')),
    path('new/position', views.NewPosition.as_view(), name='new-position'),
    path('admin/', admin.site.urls),
]
