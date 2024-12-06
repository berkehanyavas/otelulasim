from django.shortcuts import render, redirect
from .forms import JobEkleForm
from django.contrib import messages
from .models import Passenger
from otel.models import Pricing
import json
from decimal import Decimal
from job.models import Job

# Create your views here.

def ekle(request):
    if not request.user.is_authenticated:
        messages.warning(request,'Giriş yapmadan bu sayfayı göremezsiniz.')
        return redirect('/user/login')
    
    pricing = Pricing.objects.filter(
        otel = request.user.userprofile.otel
    )
    pricing_list = list(pricing.values())
    for price in pricing_list:
        if isinstance(price['price'], Decimal):
            price['price'] = float(price['price'])
            
    pricing_list.reverse()
    
    form = JobEkleForm(request.POST or None)
    
    if form.is_valid():
        passenger_names = request.POST.getlist('name_passenger')
        passenger_surnames = request.POST.getlist('surname_passenger')
        
        job_price = request.POST.get('hidden_price')
        job_currency = request.POST.get('hidden_currency')
        
        if len(passenger_names) != len(passenger_surnames):
            messages.warning(request,'Bir hata oluştu.')
            return redirect('/job/ekle')
        
        job = form.save(commit=False)
        job.created_by = request.user
        job.price = job_price
        job.currency = job_currency
        job.save()
        
        for i in range(len(passenger_names)):
            psngr = Passenger(
                job = job,
                name = passenger_names[i],
                surname = passenger_surnames[i]
            )
            psngr.save()
        
        messages.success(request,'Görev başarıyla kaydedildi.')
        return redirect('/job/ekle')
    
    context = {
        'form':form,
        'price':pricing.first(),
        'prices':json.dumps(pricing_list)
    }
    return render(request,'ekle_job.html',context)

def profil(request, id):
    if not request.user.is_authenticated:
        messages.warning(request,'Giriş yapmadan bu sayfayı göremezsiniz.')
        return redirect('/user/login')
    
    try:
        job = Job.objects.get(
            id = id
        )
    except Exception as e:
        messages.warning(request,'Bir hata oluştu.')
        return redirect('/')
    
    if request.user.userprofile.is_admin == False and request.user.userprofile.otel != job.created_by.userprofile.otel:
        messages.warning(request,'Yetkisiz giriş')
        return redirect('/')
    
    passengers = Passenger.objects.filter(
        job = job
    )
    
    context = {
        'job':job,
        'passengers':passengers,
        'no_nav':True
    }
    return render(request,'profil_job.html',context)