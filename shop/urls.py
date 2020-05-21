from rest_framework import routers
from shop import views
from django.urls import path, include

from .views import index, doc

router = routers.DefaultRouter()
router.register(r'buku', views.BukuViewSet)
router.register(r'cart', views.CartViewSet)
router.register(r'cart_detail', views.CartDetailViewSet)
router.register(r'kategori', views.KategoriViewSet)
router.register(r'pembeli', views.PembeliViewSet)
router.register(r'penulis', views.PenulisViewSet)
router.register(r'penerbit', views.PenerbitViewSet)

urlpatterns = [
    path('', index),
    path('documentation/',doc)
]
