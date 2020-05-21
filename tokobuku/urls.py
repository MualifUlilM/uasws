"""tokobuku URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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

from rest_framework import routers
from shop import views

# from django.contrib.staticfiles.urls import staticfile_urlpatterns

router = routers.DefaultRouter()
router.register(r'buku', views.BukuViewSet)
router.register(r'cart', views.CartViewSet)
router.register(r'cart_detail', views.CartDetailViewSet)
router.register(r'kategori', views.KategoriViewSet)
router.register(r'pembeli', views.PembeliViewSet)
router.register(r'penulis', views.PenulisViewSet)
router.register(r'penerbit', views.PenerbitViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('', include('shop.urls')),
]

# urlpatterns += staticfile_urlpatterns()
