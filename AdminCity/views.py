from django.shortcuts import render,redirect
from django.core.files.storage import FileSystemStorage
from django.utils.crypto import get_random_string
import os
from django.conf import settings
from .models import City
from AdminState.models import State
from django.http import HttpResponse
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt



def customcity(request):
    data = City.objects.all()
    context={
        "citydata":data
    }
    return render(request,'city.html',context)

def AddCity(request):
    if request.method == "GET":
        data = State.objects.all()
        context = {
            "statedata":data
        }
        return render(request,'addcity.html',context)
    else:
        # form value get
        name = request.POST.get("txtname")
        shippingcharge = request.POST.get("shippingcharge")
        # Insert
        sid = request.POST.get("txtstate")
        obj = City()
        obj.city_name = name
        obj.shipping_charge = shippingcharge
        obj.state_id = State.objects.get(state_id = sid)
        obj.save()
        return redirect('/back/city')
    
def deleteCity(request,id):
    obj = City.objects.get(city_id = id)
    obj.delete()
    return redirect("/back/city")

def updateCity(request,id):
    if request.method == "GET":
        data = City.objects.get(city_id = id)
        data1 = State.objects.all()
        context = {
            "data":data,
            "statedata":data1
        }
        return render(request,'updatecity.html',context)
    else:
        obj = City.objects.get(city_id = id)
        obj.city_name = request.POST.get("txtname")
        obj.shipping_charge = request.POST.get("shippingcharge")
        obj.state_id = State.objects.get(state_id = request.POST.get("txtstate"))
        obj.save()

    return redirect("/back/city")

@csrf_exempt
def loadcitybystate(request):
    sid = request.POST.get('sid')
    data = City.objects.filter(state_id = sid).values()
    json = list(data)
    return JsonResponse(json,safe=False)


@csrf_exempt
def loadcitydata(request):
    cid = request.POST.get('cid')
    data = City.objects.filter(city_id = cid).values()
    json = list(data)
    return JsonResponse(json,safe=False)