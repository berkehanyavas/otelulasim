from django.urls import path
from . import views

app_name = 'vehicle'

urlpatterns = [
    path('ekle/', views.ekle, name='ekle'),
    # path('logout/',views.logoutUser,name='logout')
]
