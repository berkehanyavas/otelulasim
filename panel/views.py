from django.shortcuts import render,redirect
from django.contrib import messages

from vehicle.models import Vehicle
from otel.models import Otel

# Create your views here.

def panel(request):
    if not request.user.is_authenticated:
        messages.warning(request,'Giriş yapmadan bu sayfayı göremezsiniz.')
        return redirect('/user/login')
    
    if request.user.userprofile.is_admin == False:
        messages.warning(request,'Yetkisiz giriş.')
        return redirect('/')
    
    vehicles = Vehicle.objects.filter(
        owner = request.user
    )
    otels = Otel.objects.filter(
        created_by = request.user
    )
    
    context = {
        'vehicles':vehicles,
        'otels':otels
    }
    return render(request,'panel.html',context)