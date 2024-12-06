from django.urls import path
from . import views

app_name = 'job'

urlpatterns = [
    path('ekle/', views.ekle, name='ekle'),
    path('<int:id>/',views.profil,name='profil')
]
