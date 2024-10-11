from django.shortcuts import render
from .models import Items


# Create your views here.
def ProductItems(request,id):
    data = Items.objects.filter(order_id = id)
    context = {
        "itemdata":data,
    }
    return render(request,'Items.html',context)