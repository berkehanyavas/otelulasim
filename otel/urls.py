from django.urls import path
from . import views

app_name = 'otel'

urlpatterns = [
    path('ekle/', views.ekle, name='ekle'),
    path('<int:id>/',views.profil,name='profil'),
    path('<int:id>/guncelle',views.guncelle,name='guncelle'),
    path('<int:id>/kullanici_ekle',views.kullanici_ekle,name='kullanici_ekle'),
]
