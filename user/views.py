from django.shortcuts import render,redirect
from .forms import LoginForm
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash

# Create your views here.

def loginUser(request):
    if request.user.is_authenticated:
        messages.warning(request,'Cikis yapmadan bu sayfayi goremezsiniz.')
        return redirect('/')

    form = LoginForm(request.POST or None)
    context = {
        'sayfaadi': 'Giris Yap',
        'form': form
    }
    
    if form.is_valid():
        username = form.cleaned_data.get('username').lower()
        password = form.cleaned_data.get('password')
        
        user = authenticate(username=username,password=password)
        
        if user is None:
            messages.warning(request,'Kullanici adi veya parola hatali.')
            return redirect('/user/login')
        
        messages.success(request,'Basariyla giris yapildi.')
        login(request,user)

        return redirect('/')
    return render(request,'login.html',context)


def logoutUser(request):
    if not request.user.is_authenticated:
        # messages.warning(request,'Giris yapmadan bu sayfayi goremezsiniz.')
        return redirect('/user/login')

    logout(request)
    messages.success(request,'Basariyla cikis yaptiniz.')
    return redirect('/user/login')

def change_password(request):
    if not request.user.is_authenticated:
        messages.warning(request,'Giriş yapmadan bu sayfayı göremezsiniz.')
        return redirect('/user/login')
    
    if request.method == 'POST':
        form = PasswordChangeForm(user=request.user, data=request.POST)
        if form.is_valid():
            user = form.save()  # Şifreyi kaydeder
            update_session_auth_hash(request, user)  # Oturumu açık tutar
            messages.success(request, 'Şifreniz başarıyla güncellendi!')
            return redirect('/')  # Kullanıcının profil sayfasına yönlendir
        else:
            messages.error(request, 'Bir hata oluştu. Lütfen tekrar deneyin.')
    else:
        form = PasswordChangeForm(user=request.user)
    return render(request, 'change_password.html', {'form': form})