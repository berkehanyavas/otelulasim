from django.urls import path
from . import views

app_name = 'panel'

urlpatterns = [
    path('', views.panel, name='login'),
    # path('logout/',views.logoutUser,name='logout')
]
