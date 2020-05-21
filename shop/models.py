from django.db import models

# Create your models here.

class Pembeli(models.Model):
    # id = models.IntegerField()
    nama = models.CharField(max_length=50)
    alamat = models.TextField()

    def __str__(self):
        return self.nama
    

class Kategori(models.Model):
    # id = models.IntegerField()
    nama_kategori = models.CharField(max_length=50)

    def __str__(self):
        return self.nama_kategori
    

class Penulis(models.Model):
    # id = models.IntegerField()
    nama_penulis = models.CharField(max_length=50)
    
    def __str__(self):
        return self.nama_penulis
    

class Penebit(models.Model):
    # id = models.IntegerField()
    nama_penerbit = models.CharField(max_length=50)
    def __str__(self):
        return self.nama_penerbit

class Cart(models.Model):
    # id = models.IntegerField()
    id_pembeli = models.ForeignKey(Pembeli, on_delete=models.CASCADE)
    invoice = models.CharField(default='####',max_length=50)
    tanggal = models.DateTimeField(auto_now=False, auto_now_add=False)
    # total = models.IntegerField()

    def __str__(self):
        return self.invoice

class Buku(models.Model):
    # id = models.IntegerField()
    id_penerbit = models.ForeignKey(Penebit, on_delete=models.CASCADE)
    id_penulis = models.ForeignKey(Penulis, on_delete=models.CASCADE)
    id_kategori = models.ForeignKey(Kategori, on_delete=models.CASCADE)
    judul = models.CharField(max_length=50)
    deskripsi = models.TextField()
    halaman = models.IntegerField()
    harga = models.IntegerField()
    tahun_terbit = models.IntegerField()
    
    def __str__(self):
        return self.judul
    

class CartDetail(models.Model):
    # id = models.IntegerField()
    id_buku = models.ManyToManyField(Buku)
    id_pembeli = models.ForeignKey(Pembeli, on_delete=models.CASCADE)
