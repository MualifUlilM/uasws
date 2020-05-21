from django.shortcuts import render

# Create your views here.
from .serializers import *
from rest_framework import viewsets

def index(request):
    return render(request, 'index.html')

def doc(request):
    return render(request, 'doc.html')

class BukuViewSet(viewsets.ModelViewSet):
    queryset = Buku.objects.all()
    serializer_class = BukuSerializer

class CartViewSet(viewsets.ModelViewSet):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer

class CartDetailViewSet(viewsets.ModelViewSet):
    queryset = CartDetail.objects.all()
    serializer_class = CartDetailSerializer

class KategoriViewSet(viewsets.ModelViewSet):
    queryset = Kategori.objects.all()
    serializer_class = KategoriSerializer

class PembeliViewSet(viewsets.ModelViewSet):
    queryset = Pembeli.objects.all()
    serializer_class = PembeliSerializer

class PenulisViewSet(viewsets.ModelViewSet):
    queryset = Penulis.objects.all()
    serializer_class = PenulisSerializer

class PenerbitViewSet(viewsets.ModelViewSet):
    queryset = Penebit.objects.all()
    serializer_class = PenerbitSerializer
