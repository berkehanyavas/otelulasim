from django.urls import path
from . import views

app_name = 'user'

urlpatterns = [
    path('login/', views.loginUser, name='login'),
    path('logout/',views.logoutUser,name='logout'),
    path('forgotpassword/',views.change_password,name='forgotpassword'),
]
