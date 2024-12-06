from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import AracEkleForm

# Create your views here.

def ekle(request):
    if not request.user.is_authenticated:
        messages.warning(request,'Giriş yapmadan bu sayfayı göremezsiniz.')
        return redirect('/user/login')
    
    form = AracEkleForm(request.POST or None)
    if form.is_valid():
        arac = form.save(commit=False)
        arac.owner = request.user
        arac.save()
        
        messages.success(request,'Otel başarıyla kaydedildi.')
        return redirect('/vehicle/ekle')
    
    context = {
        'form':form
    }
    return render(request,'ekle_arac.html',context)