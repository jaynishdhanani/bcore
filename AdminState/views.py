from django.shortcuts import render,redirect
from django.core.files.storage import FileSystemStorage
from django.utils.crypto import get_random_string
import os
from django.conf import settings
from .models import State

def customstate(request):
    data = State.objects.all()
    context={
        "statedata":data
    }
    return render(request,'state.html',context)

def AddState(request):
    if request.method == "GET":
        return render(request,'addstate.html')
    else:
        # form value get
        name = request.POST.get("txtname")
        # Insert
        obj = State()
        obj.state_name = name
        obj.save()
        return redirect('/back/state')
    
def deleteState(request,id):
    obj = State.objects.get(state_id = id)
    obj.delete()
    return redirect("/back/state")

def updateState(request,id):
    if request.method == "GET":
        data = State.objects.get(state_id = id)
        context = {
            "data":data
        }
        return render(request,'updatestate.html',context)
    else:
        obj = State.objects.get(state_id = id)
        obj.state_name = request.POST.get("txtname")
        obj.save()

    return redirect("/back/state")