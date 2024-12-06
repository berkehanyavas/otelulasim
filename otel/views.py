from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import OtelEkleForm, PricingForm
from user.forms import CustomUserCreationForm
from user.models import UserProfile
from .models import Otel, Pricing
from django.contrib.auth.models import User
from job.models import Job

# Create your views here.

def ekle(request):
    if not request.user.is_authenticated:
        messages.warning(request,'Giriş yapmadan bu sayfayı göremezsiniz.')
        return redirect('/user/login')
    
    if request.user.userprofile.is_admin == False:
        messages.warning(request,'Yetkisiz giriş.')
        return redirect('/')
    
    otelform = OtelEkleForm(request.POST or None)
    userform = CustomUserCreationForm(request.POST or None)
    pricingform = PricingForm(request.POST or None)
    if otelform.is_valid() and userform.is_valid() and pricingform.is_valid():
        max_people_list = request.POST.getlist('max_people')
        min_people_list = request.POST.getlist('min_people')
        price_list = request.POST.getlist('price')
        currency_list = request.POST.getlist('currency')
        
        if len(max_people_list) == len(min_people_list) == len(price_list) == len(currency_list):
            pass
        else:
            messages.warning(request,'Bir hata oluştu.')
            return redirect('/otel/ekle')
        
        otel = otelform.save(commit=False)
        otel.created_by = request.user
        otel.save()
        
        new_user = userform.save(commit=False)
        new_user.save()
        
        for i in range(len(min_people_list)):
            _max = max_people_list[i]
            if max_people_list[i] == '' or max_people_list[i] == '0':
                _max = 0
            price = Pricing(
                otel = otel,
                min_people = int(min_people_list[i]),
                max_people = int(_max),
                price = price_list[i],
                currency = currency_list[i]
            )
            price.save()

        new_userprofile = UserProfile(
            user = new_user,
            is_admin = False,
            otel = otel,
            created_by = request.user,
            is_forgot_pw = False,
            is_deleted = False
        )
        new_userprofile.save()
        
        messages.success(request,'Otel kullanıcısı başarıyla kaydedildi.')
        return redirect('/otel/ekle')
    
    context = {
        'otelform':otelform,
        'userform':userform,
        'pricingform':pricingform
    }
    return render(request,'ekle_otel.html',context)

def profil(request,id):
    if not request.user.is_authenticated:
        messages.warning(request,'Giriş yapmadan bu sayfayı göremezsiniz.')
        return redirect('/user/login')
    
    try:
        otel = Otel.objects.get(
            id = id
        )
    except:
        messages.warning(request,'Böyle bir otel bulunamadı.')
        return redirect('/panel')
    
    if otel.created_by != request.user:
        messages.warning(request,'Yetkisiz giriş!')
        return redirect('/')
    
    pricing = Pricing.objects.filter(
        otel = otel
    )
    
    users = User.objects.filter(
        userprofile__otel = otel
    )
    
    jobs = Job.objects.filter(
        created_by__in = users
    )
    
    context = {
        'users':users,
        'jobs':jobs,
        'otel':otel,
        'pricings':pricing
    }
    return render(request,'profil_otel.html',context)

def guncelle(request, id):
    if not request.user.is_authenticated:
        messages.warning(request,'Giriş yapmadan bu sayfayı göremezsiniz.')
        return redirect('/user/login')

    try:
        otel = Otel.objects.get(
            id = id
        )
    except Exception as e:
        messages.warning(request,'Otel bulunamadı.')
        return redirect('/')

    if otel.created_by != request.user:
        messages.warning(request,'Yetkisiz giriş.')
        return redirect('/')
    
    prices = Pricing.objects.filter(
        otel = otel
    )
    
    if request.method == 'POST':
        max_people_list = request.POST.getlist('max_people')
        min_people_list = request.POST.getlist('min_people')
        price_list = request.POST.getlist('price')
        currency_list = request.POST.getlist('currency')
        price_id_list = request.POST.getlist('price_id')
        
        if len(max_people_list) == len(min_people_list) == len(price_list) == len(currency_list):
            pass
        else:
            messages.warning(request,'Bir hata oluştu.')
            return redirect('/otel/ekle')
        
        otel_isim = request.POST.get('name')
        otel_phone = request.POST.get('phone')
        
        otel.name = otel_isim
        otel.phone = otel_phone

        otel.save()
        
        for i in range(len(min_people_list)):
            _max = max_people_list[i]
            if max_people_list[i] == '' or max_people_list[i] == 0:
                _max = 0
            try:
                price = Pricing.objects.get(
                    id = price_id_list[i]
                )
            except:
                if min_people_list[i] == '':
                    # messages.warning(request,'Bir hata oluştu')
                    # return redirect(f'/otel/{otel.id}/guncelle')
                    break
                price = Pricing(
                    otel = otel
                )
            
            price.min_people = min_people_list[i]
            price.max_people = _max
            price.price = price_list[i].replace(',','.')
            price.currency = currency_list[i]
            price.save()
            
        messages.success(request,'Bilgiler başarıyla kaydedildi.')
        return redirect(f'/otel/{otel.id}/guncelle')
    
    context = {
        'prices':prices,
        'otel':otel
    }
    return render(request,'otel_guncelle.html',context)

def kullanici_ekle(request, id):
    if not request.user.is_authenticated:
        messages.warning(request,'Giriş yapmadan bu sayfayı göremezsiniz.')
        return redirect('/user/login')

    try:
        otel = Otel.objects.get(
            id = id
        )
    except Exception as e:
        messages.warning(request,'Otel bulunamadı.')
        return redirect('/')

    if otel.created_by != request.user:
        messages.warning(request,'Yetkisiz giriş.')
        return redirect('/')
    
    form = CustomUserCreationForm(request.POST or None)
    if form.is_valid():
        new_user = form.save(commit=False)
        new_user.username = new_user.username.lower()
        new_user.save()
        
        new_userprofile = UserProfile(
            user = new_user,
            is_admin = False,
            otel = otel,
            created_by = request.user,
            is_forgot_pw = False,
            is_deleted = False
        )
        new_userprofile.save()
        
        messages.success(request,'Otel kullanıcısı başarıyla kaydedildi.')
        return redirect(f'/otel/{id}/kullanici_ekle')
    
    context = {
        'form':form
    }
    return render(request,'kullanici_ekle.html',context)