from .models import Cart
from .models import Buku
from .models import CartDetail
from .models import Kategori 
from .models import Pembeli
from .models import Penebit
from .models import Penulis 

from rest_framework import serializers

class BukuSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Buku
        fields = '__all__'

class CartSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Cart
        fields = '__all__'

class CartDetailSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = CartDetail
        fields = '__all__'

class KategoriSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Kategori
        fields = '__all__'

class PembeliSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Pembeli
        fields = '__all__'

class PenerbitSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Penebit
        fields = '__all__'

class PenulisSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Penulis
        fields = '__all__'