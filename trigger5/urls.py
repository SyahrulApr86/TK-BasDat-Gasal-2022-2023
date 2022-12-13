from django.urls import path
from trigger5.views import *

app_name = 'trigger5'

urlpatterns = [
    path('buatkategori/', buat_kategori, name='buat_kategori'),
    path('daftarkategori/', daftar_kategori, name='daftar_kategori'),
    path('pemesanankurir/', pemesanan_kurir, name='pemesanan_kurir'),
    #path('detailpemesanankurir/', detail_pemesanan_kurir, name='detail_pemesanan_kurir'),
    path('buatbahanmakanan/', buat_bahanmakanan, name='buat_bahanmakanan'),
    path('daftarbahanmakanan/', daftar_bahanmakanan, name='daftar_bahanmakanan'),
    path('daftarkategori/hapus-kategori/<int:id>', hapus_kategori, name='hapus_kategori'),
    path('daftarbahanmakanan/hapus-bahanmakanan/<int:id>', hapus_bahanmakanan, name='hapus_bahanmakanan'),
    path('pemesanankurir/selesai/<str:id>', selesai_pemesanan, name='selesai_pemesanan'),
    path('pemesanankurir/detail/<str:id>', detail_pemesanan, name='detail_pemesanan'),
]