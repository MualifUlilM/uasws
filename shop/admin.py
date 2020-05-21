from django.contrib import admin

from .models import Cart
from .models import Buku
from .models import CartDetail
from .models import Kategori 
from .models import Pembeli
from .models import Penebit
from .models import Penulis 

# Register your models here.
admin.site.register(Buku)
admin.site.register(CartDetail)
admin.site.register(Cart)
admin.site.register(Kategori)
admin.site.register(Penebit)
admin.site.register(Penulis)
admin.site.register(Pembeli)

